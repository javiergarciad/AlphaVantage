$(document).ready(function () {
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

  // delete tickets
  $("#tickets_table tbody").on("click", "#delete-botton", function () {
    var row = table.row($(this).parents("tr")).data();
    // alert("Do you want to delete: " + row.ticket + "?");
    $.post("/api/delete_ticket", { ticket: row.ticket }, function (data) {
      table.ajax.reload();
    });
  });

  // add tickets
  $(document).on("submit", "#add_ticket_form", function (e) {
    e.preventDefault();

    // get the data from the form
    var data = $("#add_ticket_form").serialize();

    // clear the form
    $("#add_ticket_form").get(0).reset();

    // send the data to the server
    r = $.post("/api/add_ticket", data, function (data) {
      if (data["status"] == "success") {
        table.ajax.reload();
      } else {
        alert("Ticket '" + data["ticket"] + "' already exists.");
      }

    });
  });
});
