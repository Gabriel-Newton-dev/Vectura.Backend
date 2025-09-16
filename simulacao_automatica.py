#!/usr/bin/env python3
"""
Simulação automática na rede Stellar Testnet
Cria transações reais sem pausas
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_separator(title):
    print(f"\n{'='*70}")
    print(f" {title}")
    print(f"{'='*70}")

def print_response(response, title):
    print(f"\n{title}:")
    print(f"Status: {response.status_code}")
    if response.status_code < 400:
        result = response.json()
        print(f"✅ Sucesso: {result.get('message', 'Operação realizada')}")
        if 'transaction_id' in result:
            print(f"🔗 Transaction ID: {result['transaction_id']}")
            print(f"🌐 Verificar em: https://testnet.steexp.com/tx/{result['transaction_id']}")
        return result
    else:
        print(f"❌ Erro: {response.text}")
        return None

def criar_financiamento():
    """Cria um novo financiamento"""
    print_separator("CRIANDO FINANCIAMENTO")
    
    financiamento_data = {
        "valor_veiculo": 200000.0,
        "valor_entrada": 40000.0,
        "valor_financiado": 160000.0,
        "taxa_juros": 3.2,
        "prazo_meses": 60
    }
    
    print(f"📋 Dados do financiamento:")
    print(f"   Valor do veículo: R$ {financiamento_data['valor_veiculo']:,.2f}")
    print(f"   Valor da entrada: R$ {financiamento_data['valor_entrada']:,.2f}")
    print(f"   Valor financiado: R$ {financiamento_data['valor_financiado']:,.2f}")
    print(f"   Taxa de juros: {financiamento_data['taxa_juros']}% a.m.")
    print(f"   Prazo: {financiamento_data['prazo_meses']} meses")
    
    response = requests.post(f"{BASE_URL}/api/financiamento/", json=financiamento_data)
    result = print_response(response, "Criação de Financiamento")
    
    if result:
        return result['id']
    return None

def aprovar_na_stellar(financiamento_id):
    """Aprova financiamento na rede Stellar Testnet"""
    print_separator("APROVANDO NA REDE STELLAR TESTNET")
    
    print("🌐 Criando transação REAL na testnet...")
    print("   Valor: 0.0000001 XLM (mínimo para teste)")
    print("   Transaction ID será real e verificável no explorer")
    
    response = requests.post(f"{BASE_URL}/api/stellar/aprovar_financiamento/{financiamento_id}")
    result = print_response(response, "Aprovação na Stellar Testnet")
    
    return result

def executar_pagamento(financiamento_id):
    """Executa pagamento na rede Stellar Testnet"""
    print_separator("EXECUTANDO PAGAMENTO NA TESTNET")
    
    # Endereço de destino (pode ser qualquer endereço válido da testnet)
    destinatario = "GCKFBEIYTKP4R4M4TZQK7X2Y3Z4X5X6X7X8X9X0X1X2X3X4X5X6X7X8X9X0"
    
    payment_data = {
        "financiamento_id": financiamento_id,
        "destinatario": destinatario
    }
    
    print(f"📤 Dados do pagamento:")
    print(f"   Financiamento ID: {financiamento_id}")
    print(f"   Destinatário: {destinatario}")
    print(f"   Valor: 0.0000001 XLM (mínimo para teste)")
    print("🌐 Executando pagamento REAL na testnet...")
    
    response = requests.post(f"{BASE_URL}/api/stellar/executar_pagamento", json=payment_data)
    result = print_response(response, "Execução do Pagamento na Testnet")
    
    return result

def verificar_status(financiamento_id):
    """Verifica status do financiamento"""
    print_separator("VERIFICANDO STATUS")
    
    response = requests.get(f"{BASE_URL}/api/financiamento/{financiamento_id}")
    result = print_response(response, "Status do Financiamento")
    
    if result:
        print(f"\n📊 Resumo:")
        print(f"   ID: {result['id']}")
        print(f"   Status: {result['status_financiamento']}")
        print(f"   Valor: R$ {result['valor_financiado']:,.2f}")
        print(f"   Data criação: {result['data_criacao']}")
        if result.get('stellar_transaction_id'):
            print(f"   Transaction ID: {result['stellar_transaction_id']}")
            print(f"   🌐 Explorer: https://testnet.steexp.com/tx/{result['stellar_transaction_id']}")

def main():
    print("🚀 SIMULAÇÃO AUTOMÁTICA - REDE STELLAR TESTNET")
    print("=" * 70)
    print("Esta simulação criará transações REAIS na testnet da Stellar")
    print("Todas as transações serão visíveis no explorer da testnet")
    print("=" * 70)
    
    # 1. Criar financiamento
    financiamento_id = criar_financiamento()
    if not financiamento_id:
        print("❌ Falha ao criar financiamento")
        return
    
    # 2. Aprovar na Stellar (TRANSAÇÃO REAL)
    aprovar_na_stellar(financiamento_id)
    
    # 3. Verificar status
    verificar_status(financiamento_id)
    
    # 4. Executar pagamento (TRANSAÇÃO REAL)
    executar_pagamento(financiamento_id)
    
    # 5. Verificar status final
    verificar_status(financiamento_id)
    
    print_separator("SIMULAÇÃO CONCLUÍDA")
    print("✅ Transações reais criadas na testnet!")
    print("🔍 Verifique as transações nos exploradores:")
    print("   - Stellar Expert: https://stellar.expert/explorer/testnet/account/< sua chave publica>")
    print("   - Stellar Laboratory: https://laboratory.stellar.org/")
    print("   - Testnet Explorer: https://testnet.steexp.com/")

if __name__ == "__main__":
    main()
