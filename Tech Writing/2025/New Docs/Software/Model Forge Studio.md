<img src="Modelforge.png" alt="Modelforge Logo" width="50%">

# ModelForge Studio 
## 1. Visão Geral
O **ModelForge Studio** é o ambiente perfeito para modelagem, renderização e simulação 3D voltado para projetos de engenharia, design industrial e desenvolvimento de jogos, tudo dentro do mesmo lugar, proporcionando uma renderização em tempo real, já que ele é baseado em GPU que total compatibilidade com **OpenGL, Vulkan e DirectX 12**

## 2. Estrutura do ModelForge Studio 
| Módulo                | Função Principal                                              | Observações                                       |
| --------------------- | ------------------------------------------------------------- | ------------------------------------------------- |
| **Core Engine**       | Gerencia a renderização, física e memória gráfica.            | Implementado em C++ com suporte a multithreading. |
| **Editor UI**         | Interface de interação do usuário.                            | Desenvolvido com Qt Framework 6.                  |
| **Shader Compiler**   | Responsável por compilar shaders GLSL/HLSL para renderização. | Integração nativa com Vulkan SDK.                 |
| **Simulation Engine** | Processa cálculos de física e colisões.                       | Baseado em biblioteca Bullet Physics.             |

## 3. Etapas de operação


| Etapa | Descrição | Componente Envolvido |
|:--:|:--|:--|
| **1** | Importe um modelo 3D nos formatos `.OBJ`, `.FBX` ou `.STL`. | Interface do Usuário |
| **2** | O modelo é alocado na memória VRAM e convertido em uma malha otimizada. | **Core Engine** |
| **3** | Materiais e efeitos de luz são aplicados em tempo real durante a renderização. | **Shader Compiler** |
| **4** | São processadas colisões e movimentações físicas do modelo. | **Simulation Engine** |
| **5** | O resultado final é renderizado e exportado em `.PNG`, `.TIFF` ou `.MP4`. | **Render Output** |
