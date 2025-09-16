# 🔐 Configuração das Chaves Stellar

## 📋 **Arquivo de Ambiente Criado:**

O arquivo `environment.env` foi criado com suas chaves Stellar da testnet:

- **Chave Pública:** `< sua chave publica>`
- **Chave Secreta:** `< sua chave privada>`

## 🚀 **Como Usar:**

### **1. Instalar Dependência:**
```bash
pip install python-dotenv
```

### **2. Ativar Conexão Real (Opcional):**
```bash
python ativar_stellar_real.py
```

### **3. Executar a API:**
```bash
python main.py
```

## ⚠️ **Importante:**

### **Segurança:**
- ✅ O arquivo `environment.env` está no `.gitignore`
- ✅ As chaves não serão commitadas no Git
- ✅ Use apenas na testnet (não na mainnet)

### **Ativação das Contas:**
Se as contas não estiverem ativas na testnet:

1. **Acesse o Friendbot:** https://friendbot.stellar.org/
2. **Digite sua chave pública:** `< sua chave publica>`
3. **Clique em "Fund Account"** para receber XLM de teste

### **Verificar Saldo:**
```bash
# Via API
curl http://localhost:8000/api/stellar/saldo/< sua chave publica>

# Via Stellar Laboratory
https://laboratory.stellar.org/#account?account=< sua chave publica>
```

## 🔄 **Modos de Operação:**

### **Modo Simulação (Padrão):**
- Usa chaves aleatórias
- Não conecta à rede real
- Seguro para desenvolvimento

### **Modo Real (Ativado):**
- Usa suas chaves reais
- Conecta à testnet
- Transações reais (mas com XLM de teste)

## 🛠️ **Configuração Avançada:**

### **Para Produção:**
1. Crie chaves na mainnet
2. Atualize o `environment.env`
3. Configure `STELLAR_NETWORK=mainnet`
4. Use chaves seguras

### **Para Desenvolvimento:**
1. Use as chaves da testnet
2. Mantenha `STELLAR_NETWORK=testnet`
3. Use o Friendbot para obter XLM de teste

## 📚 **Recursos Úteis:**

- **Stellar Laboratory:** https://laboratory.stellar.org/
- **Friendbot:** https://friendbot.stellar.org/
- **Testnet Explorer:** https://testnet.steexp.com/
- **Documentação:** https://developers.stellar.org/

## 🎯 **Status Atual:**

- ✅ Chaves configuradas
- ✅ Arquivo de ambiente criado
- ✅ Código atualizado
- ⚠️ Conexão real desativada (modo simulação)
- 🔄 Pronto para ativação
