const sleep = require('../utils/sleep');
const axios = require('axios');

const get_data = async (browser, page, link_data) => {
  let data_eps = new Array();
  let links = [];
  console.log(page)
  await page.screenshot({path: 'buddy-screenshot.png'});
  console.log('chegou aqui2222')
  try {
    links = await page.evaluate(() => {
      return Array.from(document.querySelectorAll('.episodios > li > div.episodiotitle > a')).map((el) => el.href);
    });
  } catch (error) {
    return {'Error': 'WireAnimesBr' + error};
  }
  console.log(links)
  if(links){
    const page_ep = await browser.newPage();

    for (let i = 0; i < links.length; i++) {
      const link = links[i];
      await page_ep.goto(link);
      await sleep(10000);
      
      const title = await page_ep.$eval('#info > h1', el => el.textContent.trim());
      const languages = await page_ep.$$eval("#mCSB_1_container > li > a", (el) => el.map((el) => el.textContent.trim()));
      const links_video = await page_ep.$$eval(".playex > div > iframe", (el) => el.map((el) => el.src));

        try {
          for (let j = 0; j < links_video.length; j++) {
            const link_video = links_video[j];
            const language = languages[j];
            
            if(!link_video || !language) continue;

            await axios.post(`${process.env.POST_EPS}`, {
              "anime": link_data.anime,
              'title': title,
              'language': language,
              'url_video': link_video,
              'url_ref': link

            }).then(function (response) {

              console.log(`EP ${i + 1}: `, {
                "anime": link_data.anime,
                'title': title,
                'language': language,
                'url_video': link_video,
                'url_ref': link
              });

            }).catch(function (error) {
              console.log(error);
            });

          }
        } catch (error) {
          console.log('Error: WireAnimesBr: ' + error);
        }
    }
  }

  return data_eps;
}


module.exports = get_data
