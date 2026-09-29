# ProjetoV1-calculadora-salao-de-Festas
#  Calculadora de Orçamento — Espaço Garden & Villa

Projeto pessoal desenvolvido para automatizar o cálculo de orçamentos do meu salão de festas (Garden e Villa), aplicando os dados reais de uma pesquisa de mercado que realizei mapeando mais de 20 concorrentes na região.

## Sobre o projeto

Esse é um projeto de aprendizado em Python, criado com o objetivo de praticar lógica de programação enquanto resolvo um problema real do meu negócio: gerar orçamentos rápidos e consistentes para clientes, considerando espaço escolhido, quantidade de convidados, dia da semana e alojamento.

Comecei com pouca prática recente em Python e fui construindo o projeto função por função, entendendo cada conceito antes de aplicar — por isso o código evoluiu em etapas (V1 simples → V2 com dados reais e mais regras de negócio).

## Funcionalidades

- Cálculo de orçamento baseado em:
  - Número de convidados (faixas: 100, 120, 150, 180, 200)
  - Dia da semana (dia útil x fim de semana/feriado, com preços diferentes)
  - Espaço escolhido (Garden, Villa ou os dois)
  - Alojamento (conjunto para 30 pessoas, individual para até 4, ou os dois combinados)
- Desconto automático de 10% no alojamento quando contratado junto com o espaço
- Exibição do orçamento detalhado no terminal

## Tecnologias utilizadas

- Python 3.11
- Sem bibliotecas externas (100% Python padrão) — ideal para rodar sem instalação de dependências

## Sobre os preços utilizados

Os valores usados na tabela de preços vêm de uma atualização de precificação baseada em pesquisa de mercado real (concorrentes na região do Distrito Federal), corrigindo distorções identificadas — como a ausência de diferenciação entre os espaços Garden e Villa, e entre dias de semana e fins de semana.

## Como executar

```bash
git clone https://github.com/NicolasHian/[nome-do-repositorio].git
cd [nome-do-repositorio]
python orcamento.py
```

O programa vai guiar você por perguntas no terminal (convidados, dia, espaço, alojamento) e no final exibe o orçamento completo.

## O que aprendi construindo esse projeto

- Estruturação de dados com dicionários aninhados (preço por espaço → por convidados → por tipo de dia)
- Separação de responsabilidades em funções (captura de dados, cálculo, exibição)
- Boas práticas de nomenclatura e organização de código
- Validação de entrada e tratamento de casos-limite (ex: mais de 200 convidados)

## Próximos passos

- [ ] Adicionar testes automatizados
- [ ] Migrar a lógica para uma API (Flask/FastAPI)
- [ ] Criar interface web simples para uso pela equipe do salão
- [ ] Salvar orçamentos gerados em arquivo (JSON ou banco de dados)

## Autor

**Nicolas Hian**
Estudante de Análise e Desenvolvimento de Sistemas (UniCEUB) | Em busca de estágio em Back-End
[GitHub](https://github.com/NicolasHian)
