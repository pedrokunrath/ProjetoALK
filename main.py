import pyautogui
import time
import threading
import keyboard

def Parada():
    try:
        while True:
           
            print("Sistema rodando...")  
            time.sleep(1)  
            if keyboard.is_pressed('q'): 
                print("Tecla 'q' pressionada, parando o sistema.")
                break  
    except KeyboardInterrupt:
        print("Sistema interrompido pelo usuario.")

def clique():
    for i in range(1620):  
        pyautogui.click(x=430, y=442)
        time.sleep(2)

        pyautogui.click(x=797, y=300)
        time.sleep(3)

        pyautogui.click(x=1537, y=790)
        time.sleep(2)

        pyautogui.click(x=1101, y=481)
        time.sleep(3)

        pyautogui.click(x=1143, y=265)
        time.sleep(1)

        pyautogui.click(x=1269, y=346)
        time.sleep(3)
        
        time.sleep(2)
        pyautogui.scroll(-40)
        print(f"Iteracao {i+1}/1620 concluída.")
        
        if keyboard.is_pressed('q'): 
            print("Tecla 'q' pressionada, parando as iteracoes.")
            break  
def iniciar_sistema():
    
    thread_principal = threading.Thread(target=Parada)
    thread_principal.start()

   
    clique()

    thread_principal.join()

    print("Script concluido.")

if __name__ == "__main__":
    iniciar_sistema()
