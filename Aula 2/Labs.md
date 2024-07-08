# Lab 3 - Visualizando arquivos em hexadecimal
#### 1. **Abra o Debian (via WSL) e crie um arquivo contendo seu nome e sobrenome:** 

``echo -n "nome sobrenome" > arquivo.txt ``

#### **Agora execute as tarefas abaixo e veja se a saída dos três programas faz total sentido para você.** 

**a)** Inspecione o conteúdo do arquivo com o ``hexyl``. 
**b)** Inspecione o conteúdo do arquivo com o ``hd``. 
**c)** Inspecione o conteúdo do arquivo com o ``od``.

![[Pasted image 20240708113728.png]]

**a)**
![[Pasted image 20240708113836.png]]

**b)**
![[Pasted image 20240708113926.png]]

**c)**
![[Pasted image 20240708114052.png]]

#### 2. **Crie um arquivo que contenha o número 2024 (perceba que não é o texto “2024”). Para isso, use o seguinte programa em Python:**

```python
ano = 2024 
f = open("arquivo.bin", "wb") 
f.write(ano.to_bytes(4, byteorder='little')) 
f.close()
```

#### **Agora inspecione-o com qualquer visualizador hexadecimal de linha de comando e explique os bytes encontrados lá.**

![[Pasted image 20240708115723.png]]

![[Pasted image 20240708120845.png]]

---
# Lab 04 - Convertendo strings para maiúsculo

#### 1. **Escreva uma função chamada ``toup()``, na linguagem que quiser, que receba um caractere e, caso este seja minúsculo, converta-o para maiúsculo. Sua função não deve utilizar nenhuma função de conversão de caracteres para maiúsculos, mas você pode usar ``strlen()`` para obter o tamanho de uma string. Teste sua função.** 

> Se for escrever em C/C++, utilize o DevC++ em **retoolkit → Programming → DevCpp**. Abra o arquivo %userprofile%\desktop\binarios\toup.c e altere nele o que precisar. 
> Se preferir Python, abra o prompt em **retoolkit → Programming → Python Command Prompt** e depois vá até o diretório onde o esqueleto está:

```shell
cd %userprofile%/desktop/binarios 
python toup.py
```

#### **Os esqueletos não estão alterando a string. Você precisa implementar a lógica que vai realizar essa ação.** 

#### **Teste sua função com diferentes strings, de diferentes tamanhos e contendo caracteres alfanuméricos e de pontuação**

```python
def toup(s):
    temp = ""
    
    for c in s:
        if c.islower():
            c = c.upper()
        temp = temp + chr(ord(c))
    return temp

s = "menteb.in"    
print(toup(s))
```

![[Pasted image 20240708145522.png]]

---
# Lab 05 - Manipulando strings

#### **1. Abra o programa strings1.exe no HxD e responda:**

**a)** Em que offset está a string “ELFParser-NG”? 
	0001350
**b)** Que tipo de string é esta?

#### **2. Execute o programa strings2.exe e veja a string que ele exibe. Agora feche-o, abra-o no HxD e altere a string de forma que o programa exiba o seu primeiro nome (respeite o limite de caracteres da string atual).**

![[Pasted image 20240708205155.png]]

