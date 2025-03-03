$(document).ready(function () {
    // Al hacer click en el botón de editar
    $('.btn-edit').click(function () {
      var custodiamId = $(this).data('id');
      // Hacer una llamada Ajax para obtener los detalles del custodiam
      $.ajax({
        url: '/ruta/a/tu/view/de/edicion/' + custodiamId, // La URL de tu vista que retorna los datos
        method: 'GET',
        success: function (data) {
          // Rellenar el formulario con los datos del custodiam
          $('#first_name').val(data.first_name);
          $('#last_name').val(data.last_name);
          $('#phone_number').val(data.phone_number);
          $('#address').val(data.address);
          $('#reference').val(data.reference);
          $('#email').val(data.email);
          $('#position').val(data.position); // Si es necesario, agregar un select o un valor
          // Abrir el modal
          $('#editModal').modal('show');
        }
      });
    });
  });