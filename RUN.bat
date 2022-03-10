
if exist node_modules\ (
  node paste-image-server.js
) else (
  npm install && node paste-image-server.js
)