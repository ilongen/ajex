function validationForms() {
    const fileSheet = document.getElementById('fileSheet').value;

    if (fileSheet.endsWith(".xlsx")) {
        return { bool: true };
    } else if (fileSheet.endsWith(".csv")) {
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
    const formData = new FormData(form);

    if (validated.bool) {
        post_data(formData);
   }
});

async function post_data(formData) {
    const urlGet = 'api/user_data';
    const tokenCSRF = document.getElementById('csrf-token').value
    try {
        const response = await fetch(urlGet,{
            method: "POST",body:formData, headers:{'X-CSRFToken': tokenCSRF}});
        if (response.ok){
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'data.zip'; // nome do arquivo baixado
            document.body.appendChild(a);
            a.click();
            a.remove();
        }
        else {
            throw new Error(`response status: ${response.status}`);
        }
    } catch (error) {
        console.log(error);
    }
}