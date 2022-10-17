<html>
   <body>

      <form action = "http://localhost:5000/gravar" method = "POST">
         <script>
             alert("Ola mundo");
         </script>
         <?php
              echo('Ola mundo');
         ?>
         <p>Nome <input type = "text" name = "nome" /></p>
         <p>Endereco <input type = "text" name = "endereco" /></p>
         <p>Cidade<input type = "text" name = "cidade" /></p>
         <p>UF <input type ="text" name = "uf" /></p>
         <p>CEP<input type ="text" name = "cep" /></p>
         <p>Nascimento<input type ="text" name = "data" /></p>
         <p><input type = "submit" value = "Gravar" name='botao'/></p>
      </form>
   </body>
</html>