# Lab 6 - Identificando os cabeçalhos do PE 

#### 1. **Abra o programa strings1.exe no HxD (ou 010 Editor*) e responda:**

**a)** Qual o offset no arquivo da assinatura PE? DICA: No offset 0x3c há o campo uint32_t e_lfanew, que contém o offset da assinatura PE. 

> 0000003C

![[Pasted image 20240714104423.png]]

**b)** Este é um executável de 32 ou 64-bits? 
![[Pasted image 20240714110702.png]]
  32 bits
**c)** Quantas seções este executável possui? 
![[Pasted image 20240714123000.png]]
  5 seções

**d)** Quando ele foi compilado? 
![[Pasted image 20240714124327.png]]
Convertendo Big Endian para Little Endian: 
![[Pasted image 20240714124442.png]]

![[Pasted image 20240714131926.png]]

Confirmamos também convertendo o número por meio de um código:

![[Pasted image 20240714131749.png]]
> O 010 Editor não está instalado porque a versão de avaliação funciona por 30 dias. Para instalá-lo, basta abrir um Prompt de Comando ou PowerShell e comandar:

---
#  Lab 7 - Seções do PE
### **1. Abra o programa strings1.exe no DIE e responda:**

a) Quais as características da seção .text em memória? Elas fazem sentido? 

![[Pasted image 20240714184507.png]]
![[Pasted image 20240714184702.png]]
b) Em que seção a string Papo Binario está? Quais as características dela em memória? Elas fazem sentido?

![[Pasted image 20240714185230.png]]

![[Pasted image 20240714185439.png]]

● retoolkit → PE → Detect It Easy (DIE) 
○ Habilitar a caixa "Advanced" pra poder clicar no botão "PE". 
- Sections 
-  Strings
