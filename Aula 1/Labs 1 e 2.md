# Lab 1 - Sistemas de Numeração

#### 1. **Sem efetuar nenhuma conversão, conte de zero a doze em binário.**
0 - 0000  
1 - 0001  
2 - 0010  
3 - 0011  
4 - 0100  
5 - 0101  
6 - 0110  
7 - 0111  
8 - 1000  
9 - 1001  
10 - 1010  
11 - 1011  
12 - 1100

---

##### 2. **Efetue as seguintes operações e escreva o resultado em hexa:** 
- **a)** 0xf + 1 
- **b)** 0b1010 + 1 
- **c)** 0x19 + 2 
- **d)** 0x61 - 0x20

Respostas: 
- **a)** \(0xf + 1\)  
  \(0xf\) é 15 em decimal.  
  \(15 + 1 = 16\).  
  16 em hexadecimal é \(0x10\).  
  Resultado: **0x10**

- **b)** \(0b1010 + 1\)  
  \(0b1010\) é 10 em decimal.  
  \(10 + 1 = 11\).  
  11 em hexadecimal é \(0xb\).  
  Resultado: **0xb**

- **c)** \(0x19 + 2\)  
  \(0x19\) é 25 em decimal.  
  \(25 + 2 = 27\).  
  27 em hexadecimal é \(0x1b\).  
  Resultado: **0x1b**

- **d)** \(0x61 - 0x20\)  
  \(0x61\) é 97 em decimal.  
  \(0x20\) é 32 em decimal.  
  \(97 - 32 = 65\).  
  65 em hexadecimal é \(0x41\).  
  Resultado: **0x41**

---

#### 3. **Analise o seguinte programa em C:** 

```c
#include <stdio.h>

int main() {
    int esp = 0; 
    for (int i = 0; i < 8; i++) { 
        printf("%x\n", esp); 
        esp = esp + 4; 
    }
    return 0;
}
```

Que valor (em hexa) da variável esp em cada iteração do loop? 

| **i**   | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **esp** |       |       |       |       |       |       |       |       |

Resposta:

| **i**   | **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| **esp** | 0     | 4     | 8     | c     | 10    | 14    | 18    | 1c    |

# Lab 02 - Operações matemáticas

#### 1. **Converta -1 em 32-bits para hexadecimal (use complemento de dois).**
● 00000000000000000000000000000001 
● 11111111111111111111111111111110 
● 11111111111111111111111111111111 
● FFFFFFFF

#### 2. **Calcule:**
**a)** 5 | 7, com resposta em binário e decimal. 

1 0 1   5
1 1 1   7
1 1 1   7

**b)** 9 & 1, com resposta em hexadecimal.

1 0 0 1
0 0 0 1
0 0 0 1