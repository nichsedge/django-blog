$(document).ready(function () {
    search("illuminati");

    $("#cari").keyup(function (ketik) {
        search(ketik.currentTarget.value);
    });

    function search(books_name) {
        if (books_name == "") {
            books_name = "random";
        }
        $.ajax({
            type: "GET",
            url: "list/" + books_name,
            dataType: 'json',
            success: function (response) {
                $('#listBuku').empty();
                $.each(response.items, function (i) {
                });

                var string = "";
                for (let i = 0; i < 10; i++) {
                    var eachBook = response.items[i].volumeInfo;

                    var title = eachBook.title;
                    var listAuthor = "";

                    $.each(eachBook.authors, function (i) {
                        if (i == eachBook.authors.length - 1) {
                            listAuthor += eachBook.authors[i];
                        } else {
                            listAuthor += eachBook.authors[i] + ", ";
                        }
                    });

                    if (listAuthor == "")
                        listAuthor = "Tidak diketahui";


                    var publisher = eachBook.publisher;

                    var thumbnail = eachBook.imageLinks.thumbnail;

                    $("#listBuku").append(
                        "<tr>" + "<td>" + title + "</td>"
                        + "<td>" + listAuthor + "</td>" +
                        "<td>" + publisher + "</td>" +
                        "<td>" + "<img src = '" + thumbnail + "'> </td>"
                        + "</tr>"
                    );
                }
            }
        });
    }
});

