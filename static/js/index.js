$(document).ready(function () {

  $("form#vSearchForm").submit(function (e) {
    e.preventDefault();
    var formData = new FormData(this);

    $.ajax({
      url: '/api/v1/email/v_search',
      type: 'POST',
      data: formData,
      success: function (data) {
        processQueryResult(data);
      },
      error: function (data) {
        alert('Request failed.\n' + data.responseText);
        console.log(data);
      },
      cache: false,
      contentType: false,
      processData: false
    });
  });
});


function processQueryResult(data) {
  console.log(data);
  var emails = data.result;

  $('ul#emailList').empty();
  emails.map(emailToElement);

}

function emailToElement(p) {
  var li = $("<li>", { class: "list-group-item" });
  var tbl = $('<table class="table"/>')
  var tbody = $('<tbody>')

  li.append(tbl);
  tbl.append(tbody)

  tbody.append('<tr class="btn-primary"><th scope="row">Subject</th><td>' + p.subject + '</td>')
  tbody.append('<tr><th scope="row">To</th><td>' + p.em_to + '</td>')
  tbody.append('<tr><th scope="row">Date</th><td>' + p.send_date + '</td>')
  tbody.append('<tr><th scope="row">Content</th><td>' + p.content + '</td>')

  $('ul#emailList').append(li);
}
