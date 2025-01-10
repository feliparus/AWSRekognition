# Projeto AWS Rekognition - Reconhecimento de Celebridades com AWS Rekognition

Este script processa imagens localizadas na pasta images/originais, utilizando o serviço **AWS Rekognition** para identificar celebridades presentes nas fotos. Após o processamento, o script destaca os rostos das celebridades detectadas com caixas e salva as imagens resultantes na pasta images/reconhecidas, adicionando o sufixo _processada ao nome dos arquivos.

O objetivo é automatizar o reconhecimento de rostos de celebridades e gerar imagens visualmente enriquecidas para análise ou exibição.

## Pré-requisitos

1. **Python 3.8 ou superior** instalado na máquina.
2. **Credenciais da AWS configuradas**. Para configurar, execute o seguinte comando:

```sh
aws configure
```
Certifique-se de ter as permissões necessárias para usar o serviço **Textract**.

3. **Ambiente virtual Python** recomendado (opcional, mas recomendado).

## Instalação

### 1. Criar um ambiente virtual (opcional):

O projeto foi executado no **ambiente base do Conda**, que é o ambiente padrão quando você instala o Conda. Não há necessidade de criar um novo ambiente isolado para rodar o projeto, mas caso prefira, você pode optar por criar um ambiente Conda dedicado.

#### Rodando no ambiente base do Conda:

Caso você já tenha o **Conda** instalado, pode rodar o projeto diretamente no ambiente base. O ambiente base é ativado automaticamente ao abrir o terminal.

#### Criando um ambiente isolado (opcional):

Se preferir criar um ambiente isolado para o projeto, você pode fazer isso com os seguintes comandos:

```sh
conda create --name meu-ambiente python=3.8
conda activate meu-ambiente
```

### 2. Instalar as dependências do projeto:
Com o ambiente ativado (seja no ambiente base ou em um novo ambiente Conda), instale as dependências do projeto com o seguinte comando:

```sh
pip install -r requirements.txt
```

### 3. Executar o projeto:
Uma vez que as dependências estejam instaladas, basta executar o script principal:

```sh
python main.py
```
