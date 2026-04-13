# Reflexão sobre o uso de Git

## O que foi difícil

O aspecto mais desafiador deste exercício foi entender, na prática, como o Git gerencia o estado do repositório ao longo do tempo, especialmente durante o uso de branches e merges. No início, eu tratava commits apenas como “salvar alterações”, sem pensar muito na intenção por trás deles. No entanto, ao precisar utilizar commits semânticos, percebi que escrever boas mensagens exige clareza sobre o que está sendo feito e por quê.

Outro ponto que exigiu tentativa e erro foi a manipulação de branches. Entender quando criar uma nova branch, como mantê-la atualizada com a main e como evitar conflitos não foi trivial. Em especial, o processo de merge me gerou dúvidas, principalmente quando precisei lidar com conflitos. Durante a resolução de conflito, tive dificuldade em compreender o papel do HEAD e como o Git decide quais mudanças priorizar. Ver os marcadores de conflito no código foi confuso no início, e precisei revisar o que cada parte representava antes de conseguir resolver corretamente.

Além disso, o uso de Pull Requests como ferramenta de organização também foi algo novo para mim. No começo, parecia apenas um passo extra, mas com o tempo percebi que ele força uma melhor organização e documentação das mudanças.

---

## O que ficou claro

Ao longo do exercício, ficou muito claro para mim que o Git não é apenas uma ferramenta de versionamento, mas também uma forma de comunicação. Os commits semânticos, por exemplo, deixam de ser apenas registros técnicos e passam a contar a história do desenvolvimento do projeto. Isso facilita tanto o entendimento próprio quanto de outras pessoas que venham a acessar o repositório.

Também entendi melhor o papel das branches como linhas de desenvolvimento independentes. Elas permitem trabalhar em funcionalidades isoladas sem afetar diretamente a versão principal do projeto. Isso trouxe uma visão mais organizada do desenvolvimento, onde cada mudança tem um contexto bem definido.

Outro ponto importante foi compreender o valor dos Pull Requests. Eles não servem apenas para revisar código, mas também para documentar decisões e justificar mudanças. Mesmo trabalhando sozinho, fazer PRs ajudou a estruturar melhor meu raciocínio antes de integrar alterações na main.

---

## O que ainda é confuso

Apesar de ter conseguido realizar todas as etapas do exercício, ainda existem pontos que não compreendo completamente. Um deles é o funcionamento interno do Git durante merges mais complexos. Eu consegui resolver conflitos manualmente, mas ainda não tenho total segurança sobre como o Git decide quando um conflito ocorre e como ele organiza as diferentes versões internamente.

Outra dúvida que permanece é sobre boas práticas em cenários maiores, como projetos com múltiplos desenvolvedores. Ainda não está totalmente claro para mim como evitar conflitos frequentes ou como estruturar branches em equipes maiores de forma eficiente.

Também tenho curiosidade sobre a diferença entre merge e rebase. Embora eu tenha ouvido falar desses conceitos, ainda não entendo bem quando usar cada um e quais são os impactos no histórico do projeto.

Por fim, senti que em alguns momentos consegui fazer algo funcionar sem entender completamente o motivo, especialmente ao lidar com comandos específicos do Git. Pretendo revisar esses pontos nas próximas semanas para consolidar melhor meu entendimento e evitar depender apenas de tentativa e erro.
