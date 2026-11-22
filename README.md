# Simulador de espelhos 4.0

Prévia 3D estática com Three.js 0.170.0 e `Reflector`. Abre diretamente no GitHub Pages, sem processo de compilação nem servidor de aplicação. A biblioteca é carregada por CDN, portanto a primeira abertura exige internet.

## Publicar quando aprovado

1. Revisar a branch `feature/simulador-3d` e testar a prévia em Safari no iPhone, Mac e navegador no Windows.
2. Mesclar esta branch à `main` somente após aprovação.
3. No repositório, abrir **Settings → Pages → Build and deployment** e selecionar **Deploy from a branch**, `main`, `/ (root)`; salvar. A publicação modifica o site público atual.
4. O `index.html` carrega `app.js` da mesma pasta. `legacy-2d.html` mantém a versão anterior acessível no repositório; a branch `backup/pre-simulador-3d` preserva o estado anterior integralmente.

## Como usar

Selecione uma parede, crie ou edite seus espelhos, e arraste a superfície reflexiva com um dedo ou mouse. Um toque fora do espelho gira a câmera; dois dedos aproximam e deslocam. O modo frontal permite posicionar com precisão usando os campos em metros. O projeto é salvo automaticamente em `localStorage`. Use **Exportar JSON** para um backup transferível; **Importar JSON** restaura uma cópia como novo projeto. **Salvar PNG** captura a vista atual.

As sete paredes iniciais têm apenas larguras e alturas conhecidas. Elas são mostradas separadamente, com posição e orientação configuráveis; nenhuma planta foi deduzida. Portas e janelas são objetos marcadores e não recortam a parede. Móveis são volumes simplificados. Espelhos usam `Reflector` com render targets que variam entre 256 e 1024 pixels por lado, ajustados à densidade da tela. Reflexos entre espelhos não são recursivos. Qualidade fotográfica e reflexos complexos dependem de renderização posterior em ferramenta como Blender. A exportação JSON guarda dimensões, materiais, objetos e posições e serve de base para um futuro conversor de cena.

## Verificação

`node --check app.js` valida a sintaxe JavaScript; a checagem de IDs do HTML encontrou os 37 elementos literais referenciados pelo código. A execução gráfica e os testes de interação no Safari/iPhone dependem de teste em aparelho. O Chromium disponível no ambiente recusou iniciar por restrição de socket; por isso não há teste visual automatizado concluído. Não foram criadas fotografias ou planta espacial.
