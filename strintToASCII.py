import sys

# resolução de um dos puzzles do site https://codingame.com

l = int(input()) # largura do texto
h = int(input()) # altura do texto
t = str(input()) # texto em unicode
a = [str(input()) for i in range(h)] # 'alfabeto' ascii inserido de acordo com a altura do texto

for i in range(h): # iterando com base na altura do texto
    for lt in t: # iterando com base no texto
        if lt >= 'a' and lt <= 'z': # minúsculo
            j = ord(lt) - ord('a') # unicode para int
        elif lt >= 'A' and lt <= 'Z': # maiúsculo
            j = ord(lt) - ord('A') # unicode para int
        else:
            j = ord('z') - ord('a')+1 # unicode para int caso seja um caracter especial
        
        for k in range(l): # iterando com base na largura
            print(a[i][j*l+k], end="") # mostrando as letras de t com base no alfabeto a
    print("") # debug