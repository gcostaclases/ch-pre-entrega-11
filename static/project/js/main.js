// Busca todos los menús de cuenta que existan en la página.
document.querySelectorAll(".account-menu").forEach((menu) => {
	// Cuando un menú se abre, cierra cualquier otro menú de cuenta.
	menu.addEventListener("toggle", () => {
		if (!menu.open) return;
		document.querySelectorAll(".account-menu").forEach((otherMenu) => {
			if (otherMenu !== menu) otherMenu.open = false;
		});
	});
});

// Cierra los menús si el usuario hace clic fuera de ellos.
document.addEventListener("click", (event) => {
	document.querySelectorAll(".account-menu[open]").forEach((menu) => {
		if (!menu.contains(event.target)) {
			menu.open = false;
		}
	});
});
