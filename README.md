# Controle de Gimbal com Haar Cascade e MQTT

Este projeto permite controlar um gimbal utilizando processamento de imagens (Haar Cascade) em um PC e comandos MQTT enviados para um Raspberry Pi. A câmera está acoplada ao gimbal, mas conectada ao PC para processamento.

## Requisitos

1. **PC com câmera**:
   - A câmera deve estar conectada ao PC, embora esteja fisicamente dentro do gimbal.
   
2. **Raspberry Pi**:
   - Controlará os motores do gimbal e receberá os comandos via MQTT.

3. **Dependências instaladas**:
   - No PC:
     - Python 3.x
     - OpenCV
     - Biblioteca MQTT (p. ex., `paho-mqtt`)
   - No Raspberry Pi:
     - Python 3.x
     - Biblioteca MQTT (p. ex., `paho-mqtt`)

4. **Configuração MQTT**:
   - Certifique-se de ajustar as configurações do servidor MQTT (host, porta, tópicos, etc.) em ambos os scripts.

## Configuração

1. **Prepare o PC**:
   - Conecte a câmera ao PC.
   - Certifique-se de que todas as dependências necessárias estejam instaladas.
   - Navegue até o diretório `prototype/` no projeto.

2. **Configure o Raspberry Pi**:
   - Certifique-se de que o Raspberry Pi esteja configurado para controlar o gimbal.
   - Ajuste as configurações de MQTT no script `mqtt_controll.py`.

## Como Executar

### No PC
1. Navegue até o diretório `prototype/`.
2. Execute o script de controle com Haar Cascade:
   ```bash
   python controllWithHaarCascade.py