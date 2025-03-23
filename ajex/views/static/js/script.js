function validationForms() {
    const fileSheet = document.getElementById('fileSheet').value;

    if (fileSheet.endsWith(".xlsx")) {
        let msg = "Arquivo enviado com sucesso!";
        console.log(msg);
        document.getElementById('nameSheet').value = fileSheet
        return { bool: true };
    }
    else if (fileSheet.endsWith(".csv")) {
        let msg = "Arquivo enviado com sucesso!";
        console.log(msg);
        return { bool: true };
    }
    else {
        window.alert("ERRO DE ENVIAR ARQUIVO, ESSE ARQUIVO NÃO É COMPATIVEL");
        return false;
    }
}

// Form validation input with function up
const form = document.querySelector('form[name="formPost"]');

form.addEventListener("submit", function(event) {
    event.preventDefault(); // Canceling the Standard Event

    const validated = validationForms(); // Performing the Validation Function

    if (validated) {
        form.submit();
    }
});
