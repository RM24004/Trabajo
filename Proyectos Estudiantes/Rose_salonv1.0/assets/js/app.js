/* =============================================
   ROSE BEAUTY - JAVASCRIPT PRINCIPAL
   ============================================= */

document.addEventListener('DOMContentLoaded', function () {

    // =============================================
    // CARRITO DE COMPRAS
    // =============================================

    let carrito = JSON.parse(localStorage.getItem('carritoRoseBeauty')) || [];

    function guardarCarrito() {
        localStorage.setItem('carritoRoseBeauty', JSON.stringify(carrito));
        actualizarContador();
    }

    function actualizarContador() {
        const contador = document.getElementById('carritoContador');
        const totalItems = carrito.reduce((sum, item) => sum + item.cantidad, 0);
        if (contador) {
            contador.textContent = totalItems;
        }
    }

    function renderizarCarrito() {
        const lista = document.getElementById('listaCarrito');
        const totalDiv = document.getElementById('totalCarrito');

        if (!lista || !totalDiv) return;

        if (carrito.length === 0) {
            lista.innerHTML = '<p class="carrito-vacio">Tu carrito está vacío</p>';
            totalDiv.textContent = 'Total: $0.00';
            return;
        }

        let html = '';
        let total = 0;

        carrito.forEach(function (item, index) {
            const subtotal = item.precio * item.cantidad;
            total += subtotal;
            html += `
                <div class="contenido-carrito">
                    <img src="${item.imagen}" alt="${item.nombre}" class="img-carrito">
                    <div class="info-carrito">
                        <h4>${item.nombre}</h4>
                        <span class="precio-carrito">$${item.precio.toFixed(2)}</span>
                        <div class="cantidad-controles">
                            <button class="btn-cantidad" data-index="${index}" data-action="menos">-</button>
                            <span>${item.cantidad}</span>
                            <button class="btn-cantidad" data-index="${index}" data-action="mas">+</button>
                        </div>
                    </div>
                    <button class="btn-eliminar" data-index="${index}">Eliminar</button>
                </div>
            `;
        });

        lista.innerHTML = html;
        totalDiv.textContent = 'Total: $' + total.toFixed(2);

        lista.querySelectorAll('.btn-cantidad').forEach(function (btn) {
            btn.addEventListener('click', function () {
                const index = parseInt(this.dataset.index);
                const action = this.dataset.action;
                if (action === 'mas') {
                    carrito[index].cantidad++;
                } else if (action === 'menos') {
                    carrito[index].cantidad--;
                    if (carrito[index].cantidad <= 0) {
                        carrito.splice(index, 1);
                    }
                }
                guardarCarrito();
                renderizarCarrito();
            });
        });

        lista.querySelectorAll('.btn-eliminar').forEach(function (btn) {
            btn.addEventListener('click', function () {
                const index = parseInt(this.dataset.index);
                carrito.splice(index, 1);
                guardarCarrito();
                renderizarCarrito();
            });
        });
    }

    function agregarAlCarrito(id, nombre, precio, imagen) {
        const precioNum = parseFloat(precio);
        const existente = carrito.find(function (item) { return item.id == id; });

        if (existente) {
            existente.cantidad++;
        } else {
            carrito.push({
                id: id,
                nombre: nombre,
                precio: precioNum,
                imagen: imagen,
                cantidad: 1
            });
        }

        guardarCarrito();
        renderizarCarrito();
        abrirCarrito();
    }

    function abrirCarrito() {
        const panel = document.getElementById('carritoPanel');
        if (panel) panel.classList.add('activo');
    }

    function cerrarCarrito() {
        const panel = document.getElementById('carritoPanel');
        if (panel) panel.classList.remove('activo');
    }

    // Event listeners del carrito
    document.querySelectorAll('.btn-agregar').forEach(function (btn) {
        btn.addEventListener('click', function () {
            agregarAlCarrito(this.dataset.id, this.dataset.nombre, this.dataset.precio, this.dataset.imagen);
        });
    });

    var btnCarrito = document.getElementById('btnCarrito');
    if (btnCarrito) {
        btnCarrito.addEventListener('click', function (e) {
            e.preventDefault();
            abrirCarrito();
            renderizarCarrito();
        });
    }

    var cerrarBtn = document.getElementById('cerrarCarrito');
    if (cerrarBtn) {
        cerrarBtn.addEventListener('click', cerrarCarrito);
    }

    // =============================================
    // CUPÓN DE DESCUENTO
    // =============================================

    var btnCupon = document.getElementById('btnAplicarCupon');
    if (btnCupon) {
        btnCupon.addEventListener('click', function () {
            var codigo = document.getElementById('codigoCupon').value.trim().toUpperCase();
            var msg = document.getElementById('mensajeCupon');

            if (!codigo) {
                msg.textContent = 'Ingresa un código de cupón';
                msg.className = 'mensaje-cupon error';
                return;
            }

            fetch('api/cupon.php?codigo=' + encodeURIComponent(codigo))
                .then(function (res) { return res.json(); })
                .then(function (data) {
                    if (data.exito) {
                        var total = carrito.reduce(function (sum, item) { return sum + (item.precio * item.cantidad); }, 0);
                        if (total < data.min_compra) {
                            msg.textContent = 'Compra mínima: $' + parseFloat(data.min_compra).toFixed(2);
                            msg.className = 'mensaje-cupon error';
                            return;
                        }
                        var descuento = 0;
                        if (data.tipo === 'porcentaje') {
                            descuento = total * (data.descuento / 100);
                        } else {
                            descuento = parseFloat(data.descuento);
                        }
                        var nuevoTotal = Math.max(0, total - descuento);
                        document.getElementById('totalCarrito').textContent = 'Total: $' + nuevoTotal.toFixed(2) + ' (-$' + descuento.toFixed(2) + ')';
                        msg.textContent = '¡Cupón aplicado! Descuento: $' + descuento.toFixed(2);
                        msg.className = 'mensaje-cupon exito';
                    } else {
                        msg.textContent = data.mensaje || 'Cupón inválido';
                        msg.className = 'mensaje-cupon error';
                    }
                })
                .catch(function () {
                    msg.textContent = 'Error al validar el cupón';
                    msg.className = 'mensaje-cupon error';
                });
        });
    }

    // =============================================
    // BÚSQUEDA DE PRODUCTOS
    // =============================================

    var buscador = document.getElementById('buscador');
    if (buscador) {
        var timeoutBusqueda;
        buscador.addEventListener('input', function () {
            clearTimeout(timeoutBusqueda);
            var query = this.value.trim();
            var self = this;
            timeoutBusqueda = setTimeout(function () {
                if (query.length >= 2) {
                    window.location.href = 'categorias.php?buscar=' + encodeURIComponent(query);
                }
            }, 500);
        });
    }

    // =============================================
    // POPUP NEWSLETTER
    // =============================================

    var popup = document.getElementById('popupNewsletter');
    var cerrarPopup = document.getElementById('cerrarPopup');
    var btnSuscribirse = document.getElementById('btnSuscribirse');

    if (popup && !localStorage.getItem('roseBeautySuscrito')) {
        setTimeout(function () {
            popup.classList.add('visible');
        }, 3000);
    }

    if (cerrarPopup) {
        cerrarPopup.addEventListener('click', function () {
            popup.classList.remove('visible');
        });
    }

    if (popup) {
        popup.addEventListener('click', function (e) {
            if (e.target === popup) {
                popup.classList.remove('visible');
            }
        });
    }

    if (btnSuscribirse) {
        btnSuscribirse.addEventListener('click', function () {
            var email = document.getElementById('emailCliente').value.trim();
            var cuponDiv = document.getElementById('cuponGenerado');

            if (!email || !email.includes('@')) {
                cuponDiv.textContent = 'Ingresa un correo válido';
                cuponDiv.style.color = '#e91e63';
                cuponDiv.classList.add('visible');
                return;
            }

            cuponDiv.innerHTML = '¡Gracias por suscribirte!<br>Tu cupón: <strong>BIENVENIDO10</strong>';
            cuponDiv.style.color = '#6b3d57';
            cuponDiv.classList.add('visible');
            localStorage.setItem('roseBeautySuscrito', 'true');
        });
    }

    // Inicializar
    actualizarContador();
});
