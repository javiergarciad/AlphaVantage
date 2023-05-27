$(document).ready(function () {
  // inicialize the symbols table
  var table = $("#tickets_table").DataTable({
    ajax: {
      url: "/api/tickets_info",
      dataSrc: "",
    },
    columns: [
      { data: "ticket", title: "Ticket" },
      { data: "bars", title: "# Bars" },
      { data: "updated", title: "Last Bar" },
      { data: "", title: "Actions" },
    ],
    columnDefs: [
      {
        targets: -1,
        data: null,
        defaultContent:
          '<button id="delete-botton" type="button" class="btn btn-sml"><span class="bi-trash"></span></button>\
          <button id="export-botton" type="button" class="btn btn-sml"><span class="bi bi-box-arrow-up-right"></span></button>',
      },
      {
        defaultContent: "N/A",
        targets: "_all",
      },
    ],
    order: [[1, "desc"]],
    paging: false,
    ordering: false,
    info: false,
    scrollY: "600px",
    scrollCollapse: true,
    searching: false,
  });

  // call delete tickets API
  $("#tickets_table tbody").on("click", "#delete-botton", function () {
    var row = table.row($(this).parents("tr")).data();
    $.post("/api/delete_ticket", { ticket: row.ticket }, function (data) {
      //table.ajax.reload();
      location.reload();
    });
  });

  // call export data API and save csv
  $("#tickets_table tbody").on("click", "#export-botton", function () {
    var row = table.row($(this).parents("tr")).data();
    var filename =  row.ticket + ".csv";
    $.post("/api/export_data/" + filename, { ticket: row.ticket }, function (data) {
      var blob=new Blob([data]);
      var link=document.createElement('a');
      link.href=window.URL.createObjectURL(blob);
      link.download=filename;
      link.click();
    });
  });
});
