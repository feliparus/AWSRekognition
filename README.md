# Projeto AWS Rekognition - Reconhecimento de Celebridades com AWS Rekognition

Este script processa imagens localizadas na pasta images/originais, utilizando o serviço **AWS Rekognition** para identificar celebridades presentes nas fotos. Após o processamento, o script destaca os rostos das celebridades detectadas com caixas e salva as imagens resultantes na pasta images/reconhecidas, adicionando o sufixo _processada ao nome dos arquivos.

O objetivo é automatizar o reconhecimento de rostos de celebridades e gerar imagens visualmente enriquecidas para análise ou exibição.

## Pré-requisitos

1. **Python 3.8 ou superior** instalado na máquina.
2. **Credenciais da AWS configuradas**. Para configurar, execute o seguinte comando:

```sh
aws configure
```

Certifique-se de ter as permissões necessárias para usar o serviço **Rekognition**.

3. Criar as seguintes pastas no diretório principal do projeto:

images/originais: onde as imagens originais devem ser armazenadas.

images/reconhecidas: onde as imagens processadas serão salvas.

4. (Opcional) **Ambiente virtual Python ou Conda**.

## Instalação

### 1. Configurar o ambiente virtual (opcional):

#### Caso prefira usar o ambiente base do Conda:

Se você utiliza Conda, pode rodar o projeto diretamente no ambiente base. Nesse caso, pule para o próximo passo.

#### Criando um ambiente isolado:

Se preferir, crie um ambiente dedicado para o projeto com:

```sh
conda create --name meu-ambiente python=3.8
conda activate meu-ambiente
```

### 2. Instalar as dependências do projeto:
Com o ambiente configurado e ativado, instale as dependências com:

```sh
pip install -r requirements.txt
```

### 3. Executar o projeto:
Uma vez que as dependências estejam instaladas, basta executar o script principal:

```sh
python main.py
```
