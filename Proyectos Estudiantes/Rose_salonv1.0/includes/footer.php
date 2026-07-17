</main>

<div id="carritoPanel" class="carrito-panel">
    <div class="carrito-top">
        <h2>Mi Carrito</h2>
        <button id="cerrarCarrito" class="cerrar-carrito">&times;</button>
    </div>
    <div id="listaCarrito" class="lista-carrito">
        <p class="carrito-vacio">Tu carrito está vacío</p>
    </div>
    <div id="totalCarrito" class="total-carrito">
        Total: $0.00
    </div>
    <div class="cupon-container">
        <input type="text" id="codigoCupon" placeholder="Ingresa tu cupón">
        <button id="btnAplicarCupon" class="btn-cupon">Aplicar</button>
    </div>
    <p id="mensajeCupon" class="mensaje-cupon"></p>
</div>

<div id="popupNewsletter" class="popup">
    <div class="popup-contenido">
        <span id="cerrarPopup" class="cerrar-popup">&times;</span>
        <h2>¡Bienvenido a Rose Beauty!</h2>
        <p>Suscríbete y recibe un <strong>10% de descuento</strong> en tu primera compra.</p>
        <input type="email" id="emailCliente" placeholder="Ingresa tu correo">
        <button id="btnSuscribirse" class="btn-suscribirse">Obtener Cupón</button>
        <div id="cuponGenerado" class="cupon-generado"></div>
    </div>
</div>

<footer>
    <div class="footer-contenido">
        <div class="footer-col">
            <img src="assets/img/logo-footer.png" alt="Rose Beauty" class="logo-footer">
            <p class="copyright">&copy; 2026 Rose Beauty Makeup Shop</p>
        </div>
        <div class="footer-col">
            <h4>Principal</h4>
            <ul>
                <li><a href="index.php">Inicio</a></li>
                <li><a href="categorias.php">Categorías</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Ayuda</h4>
            <ul>
                <li><a href="nosotros.php">Nosotros</a></li>
                <li><a href="terminos.php">Términos y Condiciones</a></li>
            </ul>
        </div>
        <div class="footer-col">
            <h4>Redes Sociales</h4>
            <ul>
                <li><a href="https://web.whatsapp.com/" target="_blank">WhatsApp</a></li>
                <li><a href="https://www.instagram.com/" target="_blank">Instagram</a></li>
            </ul>
        </div>
    </div>
</footer>
<script src="assets/js/app.js"></script>
</body>
</html>
