# Check Versions
_O projeto para verificar o requirements do seu projeto_

## README
- [ENGLISH](README.md) || [PORTUGUÊS](README-ptbr.md)

## Pra que serve?

 - Este projeto serve como uma forma melhor de visualizar o retorno da API do [requires.io](http://requires.io)
 - Este projeto serve como um dashboard para saber o quão atualizado o seu requirements está.

## Configurações
É necessário editar o arquivo [settings.yaml](settings.yaml)

### settings.yaml

**requires.io**
```yaml
REQUIRES_IO:
    ACTIVE: True || False # Essa config serve para indicar se vai ser usado o requires.io
    SECURITY_TOKEN: False || True # Essa config serve para quem vai usar o token via variavel de ambiente.
    USER: PUT_HERE_YOUR_USER # usuario no requires.io
    TOKEN: PUT_HERE_YOUR_TOKEN # token do requires.io caso não seja usado o SECURITY_TOKEN
    REPOSITORY_NAME: PUT_HERE_YOUR_REPOSITORY_NAME # Nome do repositoório no requires.io
    UGLIFY_REPOSITORY: False || TRUE # Essa config serve para esconder o nome do projeto, útil para projetos que não possam ser identificados no plano gratuito do requires.io
    REPOSITORY_BRANCH: master # branch utilizada no requires.io
```

**Project requirements**
```yaml
PROJECT:
  NAME: PUT_HERE_THE_PROJECT_NAME # Nome do projeto.
  REQUIREMENTS_TYPE: txt || json # Formato do requirements do projeto.
  REQUIREMENTS_URL: PUT_HERE_THE_URL # URL do requirements do projeto.
```
