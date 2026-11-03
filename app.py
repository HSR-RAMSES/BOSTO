<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sube tus fotos</title>
<style>
  body { font-family: sans-serif; background: #f2f2f2; padding: 20px; text-align: center; }
  h1 { color: #333; }
  .subir { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 2px 10px #0001; }
  input { margin: 15px 0; }
  #galeria { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px; }
  #galeria img { width: 100%; border-radius: 10px; }
  button { background: #25D366; color: white; border: none; padding: 12px 20px; border-radius: 10px; font-size: 16px; }
</style>
</head>
<body>
  <h1>📸 Mi Galería</h1>
  <div class="subir">
    <p>Selecciona fotos de tu celular</p>
    <input type="file" id="inputFotos" accept="image/*" multiple>
    <br>
    <button onclick="document.getElementById('inputFotos').click()">Subir Fotos</button>
  </div>

  <div id="galeria"></div>

<script>
  const input = document.getElementById('inputFotos');
  const galeria = document.getElementById('galeria');
  
  input.addEventListener('change', () => {
    for (let file of input.files) {
      const reader = new FileReader();
      reader.onload = e => {
        const img = document.createElement('img');
        img.src = e.target.result;
        galeria.prepend(img);
      }
      reader.readAsDataURL(file);
    }
  });
</script>
</body>
</html>

