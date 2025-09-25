document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const progressContainer = document.querySelector(".progress-container");
    const progressBar = document.getElementById("progressBar");

    // Captura o CSRF token do Django
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie("csrftoken");

    if (form && progressBar && progressContainer) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            // Mostrar barra
            progressContainer.style.display = "block";

            // Resetar barra
            progressBar.style.transition = "none";
            progressBar.style.width = "0%";
            void progressBar.offsetWidth;

            // Animar barra simulando progresso enquanto a requisição acontece
            let startTime = Date.now();
            const animationInterval = 30; // ms entre updates
            const estimatedDuration = 4000; // duração máxima simulada da barra (ms)
            
            let progress = 0;
            const interval = setInterval(() => {
                const elapsed = Date.now() - startTime;
                progress = Math.min((elapsed / estimatedDuration) * 90, 90); // nunca passa de 90% enquanto espera
                progressBar.style.width = progress + "%";
            }, animationInterval);

            // Enviar o form via fetch
            const formData = new FormData(form);
            fetch(form.action, {
                method: form.method,
                body: formData,
                headers: { "X-CSRFToken": csrftoken }
            })
            .then(response => response.blob())
            .then(blob => {
                clearInterval(interval); // para a simulação

                // Barra vai a 100%
                progressBar.style.transition = "width 300ms linear";
                progressBar.style.width = "100%";

                // Dispara o download
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.href = url;
                a.download = "dados_compactados.zip";
                document.body.appendChild(a);
                a.click();
                a.remove();
                window.URL.revokeObjectURL(url);

                // Esconde barra depois de 500ms
                setTimeout(() => {
                    progressContainer.style.display = "none";
                    progressBar.style.width = "0%";
                }, 500);
            })
            .catch(err => {
                clearInterval(interval);
                console.error("Erro na requisição:", err);
                progressContainer.style.display = "none";
                progressBar.style.width = "0%";
            });
        });
    }
});
