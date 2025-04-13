function validationForms() {
    const fileSheet = document.getElementById('fileSheet').value;

    if (fileSheet.endsWith(".xlsx")) {
        let msg = "Arquivo enviado com sucesso!";
        console.log(msg);
        document.getElementById('nameSheet').value = fileSheet;
        return { bool: true };
    } else if (fileSheet.endsWith(".csv")) {
        let msg = "Arquivo enviado com sucesso!";
        console.log(msg);
        return { bool: true };
    } else {
        window.alert("ERRO DE ENVIAR ARQUIVO, ESSE ARQUIVO NÃO É COMPATIVEL");
        return false;
    }
}

// Form validation input with function up
const form = document.querySelector('form[name="formPost"]');
form.addEventListener("submit", function(event) {
    event.preventDefault();

    const validated = validationForms();
    const url = window.location.href;
    const formData = new FormData(form);

    if (validated.bool) {
        fetch(url, {
            method: "POST",
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro no envio.");
            }
            return response.blob(); 
        })
        .then(blob => {
            console.log("Arquivo Blob recebido:", blob);  
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = "data.xlsx";
            link.style.display = 'none';
            document.body.appendChild(link);
            link.click(); // Força o download
            document.body.removeChild(link);
        })
        .catch(error => {
            console.error("Erro na requisição:", error);
        });
    }
});
