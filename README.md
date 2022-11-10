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

Utilizando-se do pattern ***Façade***, o projeto está estruturado em 3 camadas,
seguindo a arquitetura MVC.

Na **camada de visualização** temos a interface do swagger, e a própria API. Sendo
esse o método principal de interfação entre o usuário e a aplicação.

Na **camada de controle**, temos as interações com a base de dados. Utilizando
como base o SDK da AWS para interagir com o bucket que armazena os arquivos das
provas.

Por fim, na **camada de modelagem** temos os protótipos dos objetos que podem ser
utilizados na aplicação.

Essas três camadas promovem uma modularização na aplicação de tal maneira que as
responsabilidades estão divididas entre vários componentes. Facilitando a
menutenção futura. Por exemplo, caso haja necessidade de implementar um novo
método de interação com a base de dados, a lógica será de responsabilidade do
controller, e a disponibilização ao usuário atráves da API.

![image](https://user-images.githubusercontent.com/38339200/201173870-23ea975d-a7c9-4766-b549-ab10f67af644.png)

## :computer: Execução

Aplicação disponível no endereço abaixo

<https://ovbgzp3yn6.execute-api.us-east-1.amazonaws.com/docs>

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
