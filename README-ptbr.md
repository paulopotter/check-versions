# Check Versions
_Mantenha suas dependências em dia_

## README
- [ENGLISH](README.md) || **PORTUGUÊS**

## O que é isso?

 - Uma forma melhor de visualizar o retorno da API do [requires.io](http://requires.io)
 - Um dashboard para saber o quão atualizado o seu requirements está.

## Configurações
Para rodar o serviço, é necessário editar o arquivo [settings.yaml](settings.yaml)

### settings.yaml

**requires.io**
```yaml
REQUIRES_IO:
    ACTIVE: True || False # Indica se vai ser usado o requires.io
    SECURITY_TOKEN: False || True # True para quem vai passar o token via variavel de ambiente.
    USER: PUT_HERE_YOUR_USER # usuario no requires.io
    TOKEN: PUT_HERE_YOUR_TOKEN # token do requires.io, caso não seja usado o SECURITY_TOKEN
    REPOSITORY_NAME: PUT_HERE_YOUR_REPOSITORY_NAME # Nome do repositoório no requires.io
    UGLIFY_REPOSITORY: False || True # Esconder o nome do projeto no requires.io
    REPOSITORY_BRANCH: master # branch utilizada no requires.io
```

**Project requirements**
```yaml
PROJECT:
  NAME: PUT_HERE_THE_PROJECT_NAME # Nome do projeto.
  REQUIREMENTS_TYPE: txt || json # Formato do requirements do projeto.
  REQUIREMENTS_URL: PUT_HERE_THE_URL # URL do requirements do projeto.
```
