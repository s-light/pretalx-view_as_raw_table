// console.info('******************************************');
// document.addEventListener('DOMContentLoaded', function(event) {
//     console.info('DOM fully loaded and parsed.', event);
//     // init_json2table();
// });
window.addEventListener('load', function(event) {
    // console.info('All resources finished loading!', event);
    init_json2table();
}, false);

my_json2table = {}

function init_json2table() {
    console.info('init_json2table');
    my_json2table = new JSON2Table();
}

// ******************************************
// helper

function load_content(url, onload_function) {
    console.log('load_content');
    let httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        // Process the server response here.
        try {
            if (httpRequest.readyState === XMLHttpRequest.DONE) {
                if (httpRequest.status === 200) {
                    // console.log(httpRequest.responseText);
                    onload_function(httpRequest.responseText);
                } else {
                    console.error('There was a problem with the request.');
                }
            }
        }
        catch (e) {
            console.error('Caught Exception: ' + e.description);
        }
    };
    httpRequest.open(
        'GET',
        url,
        true
    );
    httpRequest.send();
}

function saveAsFile(link, content, filename, extension='.csv') {
    // https://developer.mozilla.org/en-US/docs/Web/API/Blob
    // var aFileParts = ['<a id='a'><b id='b'>hey!</b></a>'];
    // var oMyBlob = new Blob(aFileParts, {type: 'text/html'}); // the blob

    // http://stackoverflow.com/a/16330385/574981
    var blob = new Blob([content], {type: 'text/csv'});
    var url = URL.createObjectURL(blob);

    console.log('update download link:');
    const a = document.createElement('a');
    // const a = link;
    a.download = filename + extension;
    a.href = url;
    a.target = '_blank';
    // a.textContent = 'Download File';
    console.log('download link:', a);
    // console.log('open download link:', a);
    document.body.appendChild(a);
    a.click();
    a.remove();
}

// ******************************************
// main

class JSON2Table {
    constructor() {
        console.log('init');

        this.api_url = undefined;

        this.init_dom();
    }

    init_dom() {
        this.data_source_el = document.querySelector('#data_source');
        this.data_source_el.addEventListener(
            'change',
            event => this.data_source_handle_change(event)
        )
    }

    data_source_handle_change(event) {
        const new_url = this.data_source_el.value;
        if (this.api_url != new_url) {
            this.api_url = new_url;
            load_content(
                this.api_url,
                this.handle_new_data
            )
        }
    }

    handle_new_data(data) {
        console.log(data);
    }
}
