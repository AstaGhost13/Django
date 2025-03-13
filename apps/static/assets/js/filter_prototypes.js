function updatePrototypes() {
    let selectedBrand = brandSelect.val();
    prototypeSelect.empty().append('<option value="">Seleccione un modelo</option>');

    if (selectedBrand) {
        $.getJSON("{% url 'inventory:filter_prototypes' %}", { brand_id: selectedBrand }, function (data) {
            if (data.length > 0) {
                $.each(data, function (index, item) {
                    prototypeSelect.append($('<option>', {
                        value: item.id,
                        text: item.description
                    }));
                });
            } else {
                prototypeSelect.append($('<option>', {
                    value: "",
                    text: "No hay modelos disponibles para esta marca"
                }));
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.error("Error al cargar los modelos: ", textStatus, errorThrown);
            prototypeSelect.append($('<option>', {
                value: "",
                text: "Error al cargar los modelos"
            }));
        });
    }
}