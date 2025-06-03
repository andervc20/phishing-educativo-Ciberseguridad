document.addEventListener('DOMContentLoaded', function() {
    // Simulación: Mostrar advertencia si se ingresan datos
    const loginForm = document.querySelector('.login-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const token = document.getElementById('token').value;
            
            // Simulación de envío de datos (en un phishing real, se enviaría a un servidor malicioso)
            console.log('[SIMULACIÓN] Datos capturados:', { username, password, token });
            
            // Enviar formulario (redirige a /mantenimiento)
            this.submit();
        });
    }
});