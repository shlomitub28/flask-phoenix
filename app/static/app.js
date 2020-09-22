	// Get the form.
	var form = $('#ajax-contact');

	// Get the messages div.
	var formMessages = $('#form-messages');
  $('#photo').change(function() {
    $('#photo_name').val(this.files && this.files.length ? this.files[0].name : '');
  })
	// Set up an event listener for the contact form.
	$(form).submit(function(e) {
		// Stop the browser from submitting the form.
		e.preventDefault();

		// Serialize the form data.
		var formData = new FormData($(this)[0]);

		// Submit the form using AJAX.
		$.ajax({
			type: 'POST',
			url: $(form).attr('action'),
      contentType: false,
      processData: false,
			data: formData
		})
		.done(function(response) {
			// Make sure that the formMessages div has the 'success' class.
      $("#dataTable").DataTable().destroy();
      refreshTable()
      $(formMessages).removeClass('error');
			$(formMessages).addClass('success');
			// Set the message text.
			$(formMessages).text(response);
      $(form).find("input[type=text], textarea").val("");
			// Clear the form.
			$('#username').val('');
			$('#email').val('');
			$('#message').val('');
		})
		.fail(function(data) {
			// Make sure that the formMessages div has the 'error' class.
			$(formMessages).removeClass('success');
			$(formMessages).addClass('error');

			// Set the message text.
			if (data.responseText !== '') {
				$(formMessages).text(data.responseText);
			} else {
				$(formMessages).text('Oops! An error occured and your message could not be sent.');
			}
		});

	});

  $.extend( true, $.fn.dataTable.defaults, {
    "ajax": {
        "url": "/get_users",
        "type": "GET",
        "datatype": "json",
        "dataSrc": "data",

    },

    "paging":   false,
    "ordering": false,
    "info":     false,
    "searching":     false,

    "columns": [
        { "data": "username" },
        { "data": "firstname" },
        { "data": "lastname" },
        { "data": "email" },
        { "data": "telephone" },
        { "data": "message" },
        { "data": "photo", render: function (data, type, row ) { return '<img src="/get_image?username='+row.username+'">'; } }],
} );

function refreshTable(){
  $('#dataTable').DataTable();
}

$(document).ready(function () {
      refreshTable();
  });
