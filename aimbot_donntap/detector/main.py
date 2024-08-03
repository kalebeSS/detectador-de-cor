import pyautogui
import keyboard
import numpy as np

# Executa enquanto a tecla 'c' não for pressionada
while not keyboard.is_pressed('c'):
    # Captura a tela na região especificada
    sc = pyautogui.screenshot(region=(640, 390, 360, 360))
    if keyboard.is_pressed('w'):
        sc.save('teste.png')

    # Reduz a resolução da imagem para 1/32 do tamanho original
    sc = sc.resize((30, 30))  # Reduz para 1/32 do tamanho original

    # Converte a imagem para um array numpy
    sc_array = np.array(sc)

    # Varre cada pixel na área capturada
    for x in range(30):
        for y in range(30):
            # Acessa os valores de RGB diretamente do array numpy
            r, g, b = sc_array[y, x]

            # Se a cor preta for encontrada, calcula a posição original e move o mouse e clica
            if r == 0 and g == 0 and b == 0:
                # Calcula a posição original do pixel
                original_x = 640 + x * 12  # Ajuste do deslocamento horizontal
                original_y = 390 + y * 12  # Ajuste do deslocamento vertical
                pyautogui.click(original_x, original_y)
                break
        else:
            continue
        break
