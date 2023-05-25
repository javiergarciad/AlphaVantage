$(document).ready(function () {
  $("#tickets_table").DataTable({
    ajax: {
      url: "/api/tickets_info",
      dataSrc: "",
    },
    columns: [
        { data: 'ticket', title: "Ticket" },
        { data: 'bars', title: "# Bars" },
        { data: 'updated', title: "Last Updated" },
    ],
    columnDefs: [
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
});
