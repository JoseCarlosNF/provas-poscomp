# Provas POSCOMP

```
                          Universidade Federal do Pará
                    Instituto de Ciências Exatas e Naturais
                            Faculdade de Computação
                      Bacharelado em Ciência da Computação
                         Análise e Projetos de Software

                   Aluno: Jose C. N. Ferreira - 201804940020

                     Implementação Questão 4 - 2a Avaliação
```

Esse projeto viabiliza uma api para fazer download de todas as provas
disponíveis no site da Sociedade Brasileira de Computação (SBC).

> **Disclaimer**
> 
> Não há nenhum vínculo direto com a SBC, o projeto foi desenvolvido durante a
> disciplina de **Análise e Projeto de Software**, o docente reponsável por
> ministrar as aulas e a instituição não têm nenhuma responsábilidade sobre
> quaisquer aspectos legais que envolvem o projeto. Em caso de dúvidas ou
> questionamentos, entre em contato pelos meios disbilizados no perfil.

## :pushpin: UML

## :computer: Execução

# Detalhes técnicos do projeto

Nessa seção esclarece quais técnologias foram utilizadas, e como e onde estamos
rodando a aplicação.

## :whale: Build das imagens

### PROD

```
make build
```

### DEV

```
make build-dev
```

## :rocket: Como o projeto roda?

### PROD

O ambiente de produção é baseado em *serverless*, e utiliza os seguintes
recursos da AWS:

- Lambda: para rodar a app.
- API Gateway: para disponibilizar uma url de acesso.
- Bucket S3: para armazenar os aquivos.

### DEV

No ambiente local, podemos utilizar o container.

```
make dev
```
