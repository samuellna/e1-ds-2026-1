# Resolução de Conflito

O conflito ocorreu no arquivo da calculadora, na linha responsável por exibir o resultado da operação.

A branch feat/output-resultado-a utilizava a mensagem "Resultado A", enquanto a branch feat/output-resultado-b utilizava "Resultado B".

Como ambas modificavam a mesma linha, o Git não conseguiu realizar o merge automaticamente.

A resolução foi feita manualmente, optando por uma mensagem mais genérica:

print(f"Resultado: {resultado}")

Após a edição, utilizei os comandos:

git add .
git commit

para finalizar o merge.
