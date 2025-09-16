from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db, Financiamento
from models import FinanciamentoCreate, FinanciamentoUpdate, FinanciamentoResponse
from datetime import datetime
from typing import List
import subprocess
import json
import os

router = APIRouter(prefix="/api/financiamento", tags=["financiamentos"])
# ⚠️ O 'CONTRACT_ID' e a 'SECRET_KEY' devem ser armazenados de forma segura,
# idealmente usando variáveis de ambiente ou um sistema de gerenciamento de segredos.
# Não os armazene diretamente no código em produção.

CONTRACT_ID = "CDOSEAFT6X2CE6VNW4UIEQQJHKQAT3FUYVZZUMG3UPF3Z6X7DANPNJCM"

# Substitua pelo seu Secret Key
SECRET_KEY = os.environ.get("STELLAR_SECRET_KEY")

def chamar_smart_contract_aprovar(financiamento_id: int):
    """
    Chama a função 'aprovar_financiamento' no smart contract Soroban.
    
    Esta função invoca o soroban-cli para interagir com a blockchain,
    passando o ID do financiamento como um argumento.
    """
    # ⚠️ Certifique-se de que o soroban-cli esteja instalado e acessível no seu sistema.
    
    comando = [
        "soroban", "contract", "invoke",
        "--id", CONTRACT_ID,
        "--secret-key", SECRET_KEY,
        "--network", "testnet",
        "--", "aprovar_financiamento",
        "--financiamento_id", str(financiamento_id)
    ]

    try:
        resultado = subprocess.run(
            comando, 
            capture_output=True, 
            text=True, 
            check=True
        )
        print("Saída da CLI do Soroban:", resultado.stdout)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao invocar o contrato: {e.stderr}")
        raise HTTPException(
            status_code=500,
            detail=f"Falha na transação da blockchain: {e.stderr}"
        )

@router.post("/", response_model=FinanciamentoResponse, status_code=status.HTTP_201_CREATED)
async def criar_financiamento(financiamento: FinanciamentoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo registro de financiamento no banco de dados
    """
    try:
        # Validar se o valor financiado é consistente
        if financiamento.valor_financiado != (financiamento.valor_veiculo - financiamento.valor_entrada):
            raise HTTPException(
                status_code=400,
                detail="Valor financiado deve ser igual ao valor do veículo menos a entrada"
            )
        
        # Criar novo financiamento
        db_financiamento = Financiamento(
            valor_veiculo=financiamento.valor_veiculo,
            valor_entrada=financiamento.valor_entrada,
            valor_financiado=financiamento.valor_financiado,
            taxa_juros=financiamento.taxa_juros,
            prazo_meses=financiamento.prazo_meses,
            status_financiamento="pendente"
        )
        
        db.add(db_financiamento)
        db.commit()
        db.refresh(db_financiamento)
        
        return db_financiamento
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar financiamento: {str(e)}")

@router.get("/{financiamento_id}", response_model=FinanciamentoResponse)
async def obter_financiamento(financiamento_id: int, db: Session = Depends(get_db)):
    """
    Retorna os detalhes de um financiamento específico
    """
    financiamento = db.query(Financiamento).filter(Financiamento.id == financiamento_id).first()
    
    if not financiamento:
        raise HTTPException(
            status_code=404,
            detail=f"Financiamento com ID {financiamento_id} não encontrado"
        )
    
    return financiamento

@router.put("/{financiamento_id}", response_model=FinanciamentoResponse)
async def atualizar_financiamento(
    financiamento_id: int, 
    financiamento_update: FinanciamentoUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualiza o status de um financiamento e interage com o smart contract
    """
    financiamento = db.query(Financiamento).filter(Financiamento.id == financiamento_id).first()

    if not financiamento:
        raise HTTPException(
            status_code=404,
            detail=f"Financiamento com ID {financiamento_id} não encontrado"
        )
    
    # 1. Se o status for "aprovado", a API agora interage com a blockchain
    if financiamento_update.status_financiamento == "aprovado" and financiamento.status_financiamento != "aprovado":
        try:
            # Chama a função no smart contract, passando o ID do financiamento
            chamar_smart_contract_aprovar(financiamento_id)

            # Se a chamada foi bem-sucedida, atualiza o banco de dados
            financiamento.status_financiamento = "aprovado"
            financiamento.aprovado_em = datetime.utcnow()
            db.commit()
            db.refresh(financiamento)

        except HTTPException as e:
            # Se a transação falhar, a exceção já foi levantada dentro da função de chamada do contrato
            raise e
        except Exception as e:
            # Captura outros erros inesperados
            db.rollback()
            raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

    # 2. Se o status não for "aprovado", a API apenas atualiza o banco de dados localmente
    else:
        financiamento.status_financiamento = financiamento_update.status_financiamento
        db.commit()
        db.refresh(financiamento)

    return financiamento

@router.get("/status/{status}", response_model=List[FinanciamentoResponse])
async def listar_financiamentos_por_status(status: str, db: Session = Depends(get_db)):
    """
    Retorna todos os financiamentos com um determinado status
    """
    financiamentos = db.query(Financiamento).filter(
        Financiamento.status_financiamento == status
    ).all()
    
    return financiamentos

@router.get("/", response_model=List[FinanciamentoResponse])
async def listar_todos_financiamentos(db: Session = Depends(get_db)):
    """
    Retorna todos os financiamentos
    """
    financiamentos = db.query(Financiamento).all()
    return financiamentos