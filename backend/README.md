# TEMPLATE SIMPLE PYTHON

## Objetivo

Esse template cria um serviço de GET em / para responder "Hello World!!" em PYTHON e importa biblioteca request usando plugin 

## Preenchendo o YML

O arquivo YML é responsável por ter as informações necessárias para o Serverless Framework poder fazer o Deploy do serviço

```
service: node-simple-template-${env:NAME_SUFIX}
provider:
  name: aws
  stage: beta
  region: us-east-1
  runtime: python3.7

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: true

functions:
  simple:
    name: python-simple-hello
    handler: handler.hello
    events:
      - http:
          path: /
          method: GET 
```
*  `serverless-python-requirements`: plugin usado para compilar requirements em docker para poder enviar ao lambda.
*  `pythonRequirements`: configuração para usar o pip em docker e gerar as dependencias em linux-x64
*  `service`: vai ter o nome do serviço que será usado no deploy, esta sendo complementando com uma variável de ambiente para que cada um gere um deploy identificado diferente.
*  `provider`: vai conter as informações do provedor de núvem, qual linguagem, estágio(dev, beta, prod e etc...) que vai estar adicionado na url gerada
*  `functions`: vai ser passada a informação de cada endpoint para cada serviço, 
   *  `handler`: recebe o nome do arquivo(extensão) e a váriavel exportada contendo a função que vi tratar o request no formato <arquivo>.<função>
   *  `events`: tipo de acesso a função, exemplo request http
      *  `path`: caminho relativo do endpoint para o request
      *  `method`: tipo de request (GET, POST, PUT, DELETE, ANY)

## Executando

*  Rodar `npm install` para instalar as dependências, se não houver package.json, rodar `npm init --yes`
*  Caso não esteja no package.json, rodar `npm install --save serverless-python-requirements`
*  Instalar docker com `sudo apt install docker`
*  Manter as dependências do python no requirements.txt atualizado
*  Modificar o YML para suas informações
*  Fazer o deploy na núvem com o comando: `sudo sls deploy` ou `sudo sls deploy -v` caso queira informaações mais detalhadas do deploy
*  Caso use variaveis de ambiente use `sudo -E sls deploy` para manter as variáveis de ambiente do usuário
*  Ao finalizar com sucesso vai informar os endpoints criados no Api Gateway




