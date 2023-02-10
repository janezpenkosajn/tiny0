import http from 'k6/http';
import { sleep } from 'k6';
import papaparse from 'https://jslib.k6.io/papaparse/5.1.1/index.js';

const csvData = papaparse.parse(open('k6s-data.csv'), { header: true }).data;

export default function () {
  // Request page containing a form
  let res = http.get('http://localhost:5000');
  let rand = Math.floor(Math.random() * csvData.length);
  //console.log('fakeurl: ', csvData[rand].url);

  // Now, submit form setting/overriding some fields of the form
  res = res.submitForm({
    formSelector: 'form',
    fields: { url: csvData[rand].url},
  });

  //sleep(1);
}