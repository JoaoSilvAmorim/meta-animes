const sleep = require('./utils/sleep')
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

// const puppeteer = require('puppeteer-extra');
// const StealthPlugin = require('puppeteer-extra-plugin-stealth');
// const RecaptchaPlugin = require('puppeteer-extra-plugin-recaptcha');

// puppeteer.use(StealthPlugin());

// puppeteer.use(
//   RecaptchaPlugin({
//     provider: {
//       id: '2captcha',
//       token: '2d151a8e0763c46cf654cf6d44492e3a'
//     },
//     visualFeedback: false
//   })
// );

const wireAnimesBr = require('./spider/wireAnimesBr');

const runPuppeteer = async (link_data) => {
    const browser = await puppeteer.launch({
        headless: true,
        args:[
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--disable-setuid-sandbox',
            '--no-first-run',
            '--no-sandbox',
            '--no-zygote',
            '--disable-features=IsolateOrigins',
            '--disable-site-isolation-trials',
            '--ignore-certificate-errors',
        ],
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 1680, height: 1050 });
    await page.goto(link_data.url);
    await sleep(10000);
    console.log(link_data)
    try {
      const { site } = link_data;
      
      switch (site) {
        case 'ANIMESBR':
          return await wireAnimesBr(browser, page, link_data);
  
        default:
          break;
      }
    } catch (error) {
      console.log(error);
    }

    return []
}


module.exports = runPuppeteer;
