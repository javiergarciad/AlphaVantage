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
          '<button id="delete-botton" type="button" class="btn btn-sml"><span class="bi-trash"></span></button>',
          '<button id="delete-botton" type="button" class="btn btn-sml"><span class="bi-trash"></span></button>',
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
    scrollY: "200px",
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
});
