# Project to fetch latest articles from techcrunch and serve it via RestAPIs

## Architecture
- Celery is used to distribute task of fetching multiple pages from techcrunch
- Redis is used as Celery Backend but any Celery supported backend can be used.
- Postgres is used for persistent storage
![alt text](https://github.com/aniket-gupta/techcrunch-assignment/blob/main/doc/architecture-diagram.jpg?raw=true)
### Data Model
![alt text](https://github.com/aniket-gupta/techcrunch-assignment/blob/main/doc/data-model.jpg?raw=true)

## Steps To Run
- Clone the repo
```
git clone https://github.com/aniket-gupta/techcrunch-assignment.git
```
- Go to techcrunch-assignment folder
```
cd <path to git repo in your local>/techcrunch-assignment
```
- Make sure docker is running
- run docker-compose command as below:
```
docker-compose up -d --build
``` 
- server should be runnning at localhost:5000. Try below API
```
curl --location --request GET 'http://localhost:5000/api/v1/articles'
```

> Number of articles to be fetched can be configured by Environment variable `NUM_ARTICLES` default is 100

## HTTP APIs
### Get Articles
This API fetch articles stored in persistent storage<br>
Request Method: GET<br>
Path: /api/v1/articles?author_name={author_name|default None}&offset={int|default 0}&limit={int|default 10}
```
curl --location --request GET 'http://localhost:5000/api/v1/articles?offest=0&limit=1'
{
  "articles": [
    {
      "author_id": 133574468,
      "content": "<p id=\"speakable-summary\">Get your spool-of-yarn emojis ready &#8212; threads might be coming to Facebook soon. Facebook has been spotted testing a new feature that gives public figures on Facebook the ability to create a new post that&#8217;s connected to a previous one on a related subject. This feature ties the posts together more visually so fans can more easily follow updates over time. When the new post appears on followers&#8217; News Feeds, it will be shown as being connected to the other posts in a thread.</p>\n<p>Social media consultant Matt Navarra first <a href=\"https://twitter.com/MattNavarra/status/1410595945687945220\">spotted this</a> feature in action, and shared several screenshots of how it looks. Reached for comment, Facebook confirmed to TechCrunch it&#8217;s testing the feature with a small group of &#8220;public figures&#8221; on Facebook for the time being. A public figure is a specific type of Facebook Page category aimed at high-profile individuals or anyone else who wants to establish a more public presence on Facebook.</p>\n<p>&nbsp;</p><div class=\"piano-inline-promo\"></div>\n<p><div id=\"attachment_2173336\" style=\"width: 434px\" class=\"wp-caption aligncenter\"><img aria-describedby=\"caption-attachment-2173336\" loading=\"lazy\" class=\"vertical size-large wp-image-2173336\" src=\"https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?w=424\" alt=\"\" width=\"424\" height=\"680\" srcset=\"https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg 598w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=93,150 93w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=187,300 187w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=424,680 424w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=31,50 31w\" sizes=\"(max-width: 424px) 100vw, 424px\" /><p id=\"caption-attachment-2173336\" class=\"wp-caption-text\"><strong>Image Credits:</strong> Matt Navarra</p></div></p>\n<p>&nbsp;</p>\n<p>Facebook explained these threaded posts will have a &#8220;View Post Thread&#8221; button, which lets followers easily navigate to see all of the posts in the thread. When you tap on the button, you&#8217;ll be shown where you can see all the threaded posts connected together in one place.</p>\n<p>Facebook was unable to confirm if or when the test would roll out more broadly to other public figures on its platform or if it would later expand to other Page categories, like Businesses, or to Facebook Groups.</p>\n<div class=\"embed breakout\">\n<blockquote class=\"twitter-tweet\" data-width=\"550\" data-dnt=\"true\">\n<p lang=\"en\" dir=\"ltr\">Here\u2019s a few more screenshots of Facebook\u2019s NEW threaded posts feature</p>\n<p>Facebook says it\u2019s currently testing the feature with a small number of Pages for Public Figures <a href=\"https://t.co/6FktgqWMTd\">pic.twitter.com/6FktgqWMTd</a></p>\n<p>&mdash; Matt Navarra (@MattNavarra) <a href=\"https://twitter.com/MattNavarra/status/1410892166998679563?ref_src=twsrc%5Etfw\">July 2, 2021</a></p></blockquote>\n<p><script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script></div>\n<p>Threads are useful on sites like Twitter, where the character limit makes it harder to have more nuanced conversations &#8212; that&#8217;s why we end up with those oh-so-beloved &#8220;<a href=\"https://www.nytimes.com/2019/01/12/style/notes-app-celebrity-statements.html\">notes app apology</a>&#8221; posts on Twitter. (Now, Twitter promotes its <a href=\"https://techcrunch.com/2021/06/01/twitters-acquisition-strategy-eat-the-public-conversation/\">Revue</a> newsletter app when you write a thread). But on Facebook, your posts can be up to precisely 63,206 characters long (or, about 225 tweets).</p>\n<p>Rather than inspiring longer posts, Facebook threads could be used for live commentary on an event like an award show. Or, users could post updates to their existing posts in a thread, rather than updating the original and making a clunky &#8220;edited to add&#8230;&#8221; announcement. Given that Facebook is testing this feature with public figures, perhaps its intended use is to make the sharing of news more streamlined.</p>\n<p>It&#8217;s no secret that Facebook has dealt with some <a href=\"https://techcrunch.com/2020/06/26/as-advertisers-revolt-facebook-commits-to-flagging-newsworthy-political-speech-that-violates-policy/\">misinformation issues</a> in the past, so for journalists or government officials sharing information about developing news events, threads could provide useful context.</p>\n<p>This testing comes after Facebook announced its <a href=\"https://techcrunch.com/2021/06/29/facebooks-newsletter-platform-bulletin-is-now-live/\">Bulletin newsletter offshoot</a> earlier this week.</p>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"gX1zlvjuat\"><p><a href=\"https://techcrunch.com/2021/06/29/facebooks-newsletter-platform-bulletin-is-now-live/\">Facebook&#8217;s newsletter platform Bulletin is now live</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;Facebook&#8217;s newsletter platform Bulletin is now live&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2021/06/29/facebooks-newsletter-platform-bulletin-is-now-live/embed/#?secret=gX1zlvjuat\" data-secret=\"gX1zlvjuat\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n<p>&nbsp;</p>\n",
      "date": "Fri, 02 Jul 2021 19:43:55 GMT",
      "id": 2173199,
      "modified": "Fri, 02 Jul 2021 21:50:16 GMT",
      "title": "Facebook is testing a Twitter-like &#8216;threads&#8217; feature on some public figures&#8217; pages"
    }
  ],
  "limit": 1,
  "offset": 0,
  "total_articles": 100
}
```
```
curl --location --request GET 'http://localhost:5000/api/v1/articles?author_name=Amanda%20Silberling'
{
  "articles": [
    {
      "author_id": 133574468,
      "content": "<p id=\"speakable-summary\">Get your spool-of-yarn emojis ready &#8212; threads might be coming to Facebook soon. Facebook has been spotted testing a new feature that gives public figures on Facebook the ability to create a new post that&#8217;s connected to a previous one on a related subject. This feature ties the posts together more visually so fans can more easily follow updates over time. When the new post appears on followers&#8217; News Feeds, it will be shown as being connected to the other posts in a thread.</p>\n<p>Social media consultant Matt Navarra first <a href=\"https://twitter.com/MattNavarra/status/1410595945687945220\">spotted this</a> feature in action, and shared several screenshots of how it looks. Reached for comment, Facebook confirmed to TechCrunch it&#8217;s testing the feature with a small group of &#8220;public figures&#8221; on Facebook for the time being. A public figure is a specific type of Facebook Page category aimed at high-profile individuals or anyone else who wants to establish a more public presence on Facebook.</p>\n<p>&nbsp;</p><div class=\"piano-inline-promo\"></div>\n<p><div id=\"attachment_2173336\" style=\"width: 434px\" class=\"wp-caption aligncenter\"><img aria-describedby=\"caption-attachment-2173336\" loading=\"lazy\" class=\"vertical size-large wp-image-2173336\" src=\"https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?w=424\" alt=\"\" width=\"424\" height=\"680\" srcset=\"https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg 598w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=93,150 93w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=187,300 187w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=424,680 424w, https://techcrunch.com/wp-content/uploads/2021/07/E5Nxh9-VoAkVzAb.jpeg?resize=31,50 31w\" sizes=\"(max-width: 424px) 100vw, 424px\" /><p id=\"caption-attachment-2173336\" class=\"wp-caption-text\"><strong>Image Credits:</strong> Matt Navarra</p></div></p>\n<p>&nbsp;</p>\n<p>Facebook explained these threaded posts will have a &#8220;View Post Thread&#8221; button, which lets followers easily navigate to see all of the posts in the thread. When you tap on the button, you&#8217;ll be shown where you can see all the threaded posts connected together in one place.</p>\n<p>Facebook was unable to confirm if or when the test would roll out more broadly to other public figures on its platform or if it would later expand to other Page categories, like Businesses, or to Facebook Groups.</p>\n<div class=\"embed breakout\">\n<blockquote class=\"twitter-tweet\" data-width=\"550\" data-dnt=\"true\">\n<p lang=\"en\" dir=\"ltr\">Here\u2019s a few more screenshots of Facebook\u2019s NEW threaded posts feature</p>\n<p>Facebook says it\u2019s currently testing the feature with a small number of Pages for Public Figures <a href=\"https://t.co/6FktgqWMTd\">pic.twitter.com/6FktgqWMTd</a></p>\n<p>&mdash; Matt Navarra (@MattNavarra) <a href=\"https://twitter.com/MattNavarra/status/1410892166998679563?ref_src=twsrc%5Etfw\">July 2, 2021</a></p></blockquote>\n<p><script async src=\"https://platform.twitter.com/widgets.js\" charset=\"utf-8\"></script></div>\n<p>Threads are useful on sites like Twitter, where the character limit makes it harder to have more nuanced conversations &#8212; that&#8217;s why we end up with those oh-so-beloved &#8220;<a href=\"https://www.nytimes.com/2019/01/12/style/notes-app-celebrity-statements.html\">notes app apology</a>&#8221; posts on Twitter. (Now, Twitter promotes its <a href=\"https://techcrunch.com/2021/06/01/twitters-acquisition-strategy-eat-the-public-conversation/\">Revue</a> newsletter app when you write a thread). But on Facebook, your posts can be up to precisely 63,206 characters long (or, about 225 tweets).</p>\n<p>Rather than inspiring longer posts, Facebook threads could be used for live commentary on an event like an award show. Or, users could post updates to their existing posts in a thread, rather than updating the original and making a clunky &#8220;edited to add&#8230;&#8221; announcement. Given that Facebook is testing this feature with public figures, perhaps its intended use is to make the sharing of news more streamlined.</p>\n<p>It&#8217;s no secret that Facebook has dealt with some <a href=\"https://techcrunch.com/2020/06/26/as-advertisers-revolt-facebook-commits-to-flagging-newsworthy-political-speech-that-violates-policy/\">misinformation issues</a> in the past, so for journalists or government officials sharing information about developing news events, threads could provide useful context.</p>\n<p>This testing comes after Facebook announced its <a href=\"https://techcrunch.com/2021/06/29/facebooks-newsletter-platform-bulletin-is-now-live/\">Bulletin newsletter offshoot</a> earlier this week.</p>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"gX1zlvjuat\"><p><a href=\"https://techcrunch.com/2021/06/29/facebooks-newsletter-platform-bulletin-is-now-live/\">Facebook&#8217;s newsletter platform Bulletin is now live</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;Facebook&#8217;s newsletter platform Bulletin is now live&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2021/06/29/facebooks-newsletter-platform-bulletin-is-now-live/embed/#?secret=gX1zlvjuat\" data-secret=\"gX1zlvjuat\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n<p>&nbsp;</p>\n",
      "date": "Fri, 02 Jul 2021 19:43:55 GMT",
      "id": 2173199,
      "modified": "Fri, 02 Jul 2021 21:50:16 GMT",
      "title": "Facebook is testing a Twitter-like &#8216;threads&#8217; feature on some public figures&#8217; pages"
    },
    {
      "author_id": 133574468,
      "content": "<p id=\"speakable-summary\">The creator economy is changing the way that people earn a living, whether you&#8217;re an Instagram influencer or a freelance graphic designer. But traditional banks haven&#8217;t caught up.</p>\n<p>Take Alexandra Botez for example. The Stanford graduate <a href=\"https://www.cnbc.com/2021/02/19/25-year-old-earns-6-figures-playing-chess-on-twitch.html\">earns six figures</a> playing chess on Twitch, where <a href=\"https://www.twitch.tv/botezlive\">she has 877,000 followers</a>. But when she tried to apply for a business credit card, she was rejected twice. Meanwhile, when the creator behind <a href=\"https://www.youtube.com/channel/UCHsRtomD4twRf5WVHHk-cMw\">TierZoo</a>, a YouTube channel with 2.7 million subscribers, tried to rent an apartment, he was rejected because his landlord didn&#8217;t see his business as legitimate.</p>\n<p>Eric Wei noticed this disconnect while he was a product manager at Instagram, where he helped build Instagram Live. With co-founder Will Kim, a previous investor with seed fund Lucky Capital, Wei launched <a href=\"https://www.trykarat.com/\">Karat Financial</a>, a better banking system for digital creators. Today, Karat Financial announced a $26 million Series A round led by Union Square Ventures with participation from GGV Capital and SignalFire.</p><div class=\"piano-inline-promo\"></div>\n<p>&#8220;Banks need to understand you in order to trust you, and it&#8217;s only when they trust you that they&#8217;re willing to give you credit, process your payments and hold your money,&#8221; Wei told TechCrunch. &#8220;If Alexandra Botez has 800,000 followers, and let&#8217;s say a tenth of them are paying a monthly subscription fee on Twitch, you can actually back into what these creators&#8217; income streams are and develop a better underwriting model than what the banks have today.&#8221;</p>\n<p>But Karat isn&#8217;t solving a problem exclusive to the 1% of digital creators. Even for someone like a self-employed small business owner or a gig worker, it can be challenging to find a landlord that will rent an apartment without a proof of employment letter and regular paystubs. But the creator economy remains a fast-growing sector &#8212; more than <a href=\"https://www.forbes.com/sites/mattklein/2020/09/23/50m-join-the-creator-economy-as-new-platforms-emerge-to-help-anyone-produce-content--money/?sh=7ade4e813165\">two million creators</a> make over $100,000 per year, and according to VC firm SignalFire, <a href=\"https://signalfire.com/blog/creator-economy/\">over 46.7 million people</a> have enough of a following to monetize their content part time.</p>\n<p>&#8220;This whole industry exploded,&#8221; said Kim. &#8220;If it&#8217;s a flash in the pan, it&#8217;s a fifteen-year-old flash.&#8221;</p>\n<p><span style=\"font-size: 1rem; letter-spacing: -0.1px;\">Wei and Kim founded Karat in 2019, then earned a spot in <a href=\"https://techcrunch.com/2019/11/04/venture-capitalists-like-and-subscribe-to-influencers/\">Y Combinator&#8217;s Winter 2020 accelerator.</a> By June 2020, Karat launched its first product, the Karat Black Card, a credit card for creators, and earned </span><a style=\"font-size: 1rem; letter-spacing: -0.1px; background-color: #ffffff;\" href=\"https://techcrunch.com/2020/06/25/karat-black-card/\">$4.6 million in seed funding</a><span style=\"font-size: 1rem; letter-spacing: -0.1px;\"> from investors like Twitch co-founder Kevin Lin.</span></p>\n<p><div id=\"attachment_2171281\" style=\"width: 690px\" class=\"wp-caption aligncenter\"><img aria-describedby=\"caption-attachment-2171281\" loading=\"lazy\" class=\"size-large wp-image-2171281\" src=\"https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?w=680\" alt=\"\" width=\"680\" height=\"510\" srcset=\"https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png 3000w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=150,113 150w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=300,225 300w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=768,576 768w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=680,510 680w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=1536,1152 1536w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=2048,1536 2048w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=50,38 50w\" sizes=\"(max-width: 680px) 100vw, 680px\" /><p id=\"caption-attachment-2171281\" class=\"wp-caption-text\"><strong>Image Credits:</strong> Karat</p></div></p>\n<p>&#8220;Our vetting process is we try to evaluate creators as the businesses they are,&#8221; Wei said. The Karat Black Card doesn&#8217;t charge interest or fees, and only turns a marginal profit off of bank interchange fees. Karat will also advance credit for sponsorship payments at no cost to the creator. So if you&#8217;re an influencer and get paid $1,000 to make a video sponsored by a clothing company, it could take months to get paid. Karat will give you that $1,000 now, so long as you pay them back once the clothing company pays you.</p>\n<p>Karat proved its concept with 50% growth from month to month and eight figures in transactions since launch last year. More than 30 creators have invested in Karat, including <a href=\"https://twitter.com/JaredLeto?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor\">Jared Leto</a>, <a href=\"https://www.instagram.com/3lau/\">3LAU</a>, <a href=\"https://www.facebook.com/nasdaily\">Nas Daily</a>\u00a0and <a href=\"https://www.tiktok.com/@joshrichards?lang=en\">Josh Richards</a> &#8212; that&#8217;s all without any spending on influencer marketing.</p>\n<p>&#8220;It turns out that when you do a good job for creators, they share you around with other people,&#8221; Wei said.</p>\n<p><span style=\"font-size: 1rem; letter-spacing: -0.1px;\"> Since then, their portfolio of investors has grown to include YouTube co-founder Steven Chen, Twitter co-founder Biz Stone, former TikTok CEO Kevin Mayer and former Wealthfront CEO Adam Nash, among others.</span></p>\n<p>But Karat&#8217;s ultimate ambition isn&#8217;t to give creators a line of credit. They started out with the credit card to prove their concept, but in the long term, they hope to create a financial infrastructure for creators. That means helping them launch merchandise lines, incorporate their business, get a mortgage, take out business loans and file their taxes. Wei says that would come after the company&#8217;s Series B, opening a more lucrative income stream than collecting bank interchange fees.</p>\n<p>&#8220;We decided to roll Karat out with the same tried-and-true fintech playbook,&#8221; Wei said. &#8220;Start out with something simple before wedging and scaling into those other products. So for us, the card is just a means to an end. Our whole model is, we use the cards to develop our underwriting model and gain trust from creators, and eventually, we can build to be Square for creators.&#8221;</p>\n<p>Already, Wei and Kim are getting texts from their internet celebrity clients, asking them to be their de-facto financial advisers.</p>\n<p>&#8220;We&#8217;re just like, oh my gosh, we love you, but we&#8217;re not building those products yet,&#8221; Wei said. &#8220;We&#8217;ll do that when we hit our Series B, and yes, we&#8217;ll charge you fees, because we&#8217;re going to provide you with better service than what&#8217;s out there now.&#8221;</p>\n<p>With the newly announced Series A round, Karat plans to double its staff with new hires and begin looking toward new product development.</p>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"4xRlYBrb3a\"><p><a href=\"https://techcrunch.com/2021/06/17/5-tips-for-brands-that-want-to-succeed-in-the-new-era-of-influencer-marketing/\">5 tips for brands that want to succeed in the new era of influencer marketing</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;5 tips for brands that want to succeed in the new era of influencer marketing&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2021/06/17/5-tips-for-brands-that-want-to-succeed-in-the-new-era-of-influencer-marketing/embed/#?secret=4xRlYBrb3a\" data-secret=\"4xRlYBrb3a\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"e6jdzjbpxP\"><p><a href=\"https://techcrunch.com/2020/06/25/karat-black-card/\">Karat launches a credit card for online creators</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;Karat launches a credit card for online creators&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2020/06/25/karat-black-card/embed/#?secret=e6jdzjbpxP\" data-secret=\"e6jdzjbpxP\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"Yvta3LLWFv\"><p><a href=\"https://techcrunch.com/2019/11/04/venture-capitalists-like-and-subscribe-to-influencers/\">Venture capitalists \u2018like and subscribe\u2019 to influencers</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;Venture capitalists \u2018like and subscribe\u2019 to influencers&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2019/11/04/venture-capitalists-like-and-subscribe-to-influencers/embed/#?secret=Yvta3LLWFv\" data-secret=\"Yvta3LLWFv\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n",
      "date": "Thu, 01 Jul 2021 16:00:16 GMT",
      "id": 2171243,
      "modified": "Thu, 01 Jul 2021 22:22:49 GMT",
      "title": "A bank for the creator economy, Karat Financial raises $26M in Series A funding"
    },
    {
      "author_id": 133574468,
      "content": "<p id=\"speakable-summary\">Starting today, Pinterest will prohibit all advertisers from sharing ads that promote weight loss. This includes any language and imagery that encourages weight loss, promotes weight loss products, idealizes certain body types, or references the BMI (which is often <a href=\"https://elemental.medium.com/the-bizarre-and-racist-history-of-the-bmi-7d8dc2aa33bb\">a poor indicator of overall health</a>). This makes Pinterest the first major social media platform to take this stance.</p>\n<p>Social media has played a role in promoting harmful beauty standards for <a href=\"https://techcrunch.com/2013/06/20/over-a-year-after-new-content-policies-self-harm-social-media-still-thrives/\">as long as it&#8217;s existed</a>. But even as &#8220;body positivity&#8221; has eclipsed the &#8220;thinspo&#8221; that proliferated on Tumblr a decade ago, sometimes, the trend can be a thin veil for weight stigma. Take a company like Weight Watchers, for example, which <a href=\"https://slate.com/business/2021/03/weight-watchers-name-change-ww-dieting-culture.html\">re-branded</a> to WW (&#8220;Wellness That Works&#8221;) in 2018, yet continues to boast its members&#8217; weight loss stories on its website. Even when online content about weight loss is well-meaning, it often contributes to a rise in disordered eating behavior rather than healthy habits, which is why <a href=\"https://qz.com/quartzy/1256525/the-wellness-industry-thrives-on-the-fear-of-death/\">the wellness industry can be so harmful</a>.</p>\n<p>Pinterest developed its updated ad policy with guidance from the <a href=\"https://www.nationaleatingdisorders.org/\">National Eating Disorders Association</a> (NEDA), which has also worked with platforms like Tumblr and Facebook in the past. Since March 2020, the onset of the pandemic in the US, NEDA has experienced an increase in activity on its helplines for people struggling with eating disorders. As Vox&#8217;s Rebecca Jennings <a href=\"https://www.vox.com/the-goods/22226997/body-positivity-instagram-tiktok-fatphobia-social-media\">pointed out</a>, people started spending even more time online during lockdown, which means more exposure to content that <a href=\"https://techcrunch.com/2018/11/09/limiting-social-media-use-reduced-loneliness-and-depression-in-new-experiment/\">makes us feel bad</a> about ourselves. Even the TikTok-famous sixteen-year-old actress Sissy Sheridan <a href=\"https://twitter.com/sissysheridan/status/1261075790168576000\">tweeted</a>, &#8220;<span style=\"font-size: 1rem; letter-spacing: -0.1px;\">i liked my body before i downloaded tik tok.&#8221;</span></p><div class=\"piano-inline-promo\"></div>\n<p><div id=\"attachment_2172399\" style=\"width: 520px\" class=\"wp-caption aligncenter\"><img aria-describedby=\"caption-attachment-2172399\" loading=\"lazy\" class=\"size-large wp-image-2172399\" src=\"https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?w=510\" alt=\"\" width=\"510\" height=\"510\" srcset=\"https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg 510w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=150,150 150w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=300,300 300w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=32,32 32w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=50,50 50w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=64,64 64w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=96,96 96w, https://techcrunch.com/wp-content/uploads/2021/06/pinterest-bodyneutrality.jpeg?resize=128,128 128w\" sizes=\"(max-width: 510px) 100vw, 510px\" /><p id=\"caption-attachment-2172399\" class=\"wp-caption-text\"><strong>Image Credits:</strong> Pinterest</p></div></p>\n<div class=\"css-1dbjc4n\">Pinterest&#8217;s new policy can make a tangible difference, especially if it sets a precedent for other major platforms to follow suit. Social media platforms have a responsibility to minimize the harmful activity that happens on their apps, but how far can the impact of these new policies extend? Pinterest reported that searches for &#8220;body neutrality&#8221; are up 5x since last year, offering an alternative to the &#8220;body positivity&#8221; movement, which is often just diet culture in a trench coat. But especially on algorithm-driven apps like TikTok, we can&#8217;t always control the content that comes up on your For You page. If you like to cook, TikTok will show you cooking videos, but the AI isn&#8217;t smart enough to filter out cooking accounts with &#8220;weight loss&#8221; in their bios if you don&#8217;t engage with that content. Pinterest recently launched <a href=\"https://techcrunch.com/2021/05/18/pinterest-introduces-idea-pins-a-video-first-feature-aimed-at-creators/\">its own TikTok competitor</a>, and of course, Instagram is trying to capture the success of TikTok through its <a href=\"https://techcrunch.com/2021/05/24/new-instagram-insights-make-its-tiktok-competitor-reels-more-appealing/\">Reels</a>.</div>\n<div></div>\n<div class=\"css-1dbjc4n\">Pinterest&#8217;s ad policy update is a good start, and one that can only have a positive impact if other platforms follow its lead. But social media reflects our culture back to us, and until there&#8217;s a broader cultural shift to understand that &#8220;weight loss&#8221; and &#8220;wellness&#8221; aren&#8217;t synonymous, an ad policy can only go so far.</div>\n",
      "date": "Thu, 01 Jul 2021 13:13:13 GMT",
      "id": 2172123,
      "modified": "Thu, 01 Jul 2021 13:13:13 GMT",
      "title": "Pinterest updates policy to prohibit ads promoting weight loss"
    }
  ],
  "limit": 3,
  "offset": 0,
  "total_articles": 3
}
```
### Get Article by id
This API fetch article given id
Request Method: GET<br>
Path: /api/v1/articles/{article_id}
```
curl --location --request GET 'http://localhost:5000/api/v1/articles/2171243'
{
  "author_id": 133574468,
  "content": "<p id=\"speakable-summary\">The creator economy is changing the way that people earn a living, whether you&#8217;re an Instagram influencer or a freelance graphic designer. But traditional banks haven&#8217;t caught up.</p>\n<p>Take Alexandra Botez for example. The Stanford graduate <a href=\"https://www.cnbc.com/2021/02/19/25-year-old-earns-6-figures-playing-chess-on-twitch.html\">earns six figures</a> playing chess on Twitch, where <a href=\"https://www.twitch.tv/botezlive\">she has 877,000 followers</a>. But when she tried to apply for a business credit card, she was rejected twice. Meanwhile, when the creator behind <a href=\"https://www.youtube.com/channel/UCHsRtomD4twRf5WVHHk-cMw\">TierZoo</a>, a YouTube channel with 2.7 million subscribers, tried to rent an apartment, he was rejected because his landlord didn&#8217;t see his business as legitimate.</p>\n<p>Eric Wei noticed this disconnect while he was a product manager at Instagram, where he helped build Instagram Live. With co-founder Will Kim, a previous investor with seed fund Lucky Capital, Wei launched <a href=\"https://www.trykarat.com/\">Karat Financial</a>, a better banking system for digital creators. Today, Karat Financial announced a $26 million Series A round led by Union Square Ventures with participation from GGV Capital and SignalFire.</p><div class=\"piano-inline-promo\"></div>\n<p>&#8220;Banks need to understand you in order to trust you, and it&#8217;s only when they trust you that they&#8217;re willing to give you credit, process your payments and hold your money,&#8221; Wei told TechCrunch. &#8220;If Alexandra Botez has 800,000 followers, and let&#8217;s say a tenth of them are paying a monthly subscription fee on Twitch, you can actually back into what these creators&#8217; income streams are and develop a better underwriting model than what the banks have today.&#8221;</p>\n<p>But Karat isn&#8217;t solving a problem exclusive to the 1% of digital creators. Even for someone like a self-employed small business owner or a gig worker, it can be challenging to find a landlord that will rent an apartment without a proof of employment letter and regular paystubs. But the creator economy remains a fast-growing sector &#8212; more than <a href=\"https://www.forbes.com/sites/mattklein/2020/09/23/50m-join-the-creator-economy-as-new-platforms-emerge-to-help-anyone-produce-content--money/?sh=7ade4e813165\">two million creators</a> make over $100,000 per year, and according to VC firm SignalFire, <a href=\"https://signalfire.com/blog/creator-economy/\">over 46.7 million people</a> have enough of a following to monetize their content part time.</p>\n<p>&#8220;This whole industry exploded,&#8221; said Kim. &#8220;If it&#8217;s a flash in the pan, it&#8217;s a fifteen-year-old flash.&#8221;</p>\n<p><span style=\"font-size: 1rem; letter-spacing: -0.1px;\">Wei and Kim founded Karat in 2019, then earned a spot in <a href=\"https://techcrunch.com/2019/11/04/venture-capitalists-like-and-subscribe-to-influencers/\">Y Combinator&#8217;s Winter 2020 accelerator.</a> By June 2020, Karat launched its first product, the Karat Black Card, a credit card for creators, and earned </span><a style=\"font-size: 1rem; letter-spacing: -0.1px; background-color: #ffffff;\" href=\"https://techcrunch.com/2020/06/25/karat-black-card/\">$4.6 million in seed funding</a><span style=\"font-size: 1rem; letter-spacing: -0.1px;\"> from investors like Twitch co-founder Kevin Lin.</span></p>\n<p><div id=\"attachment_2171281\" style=\"width: 690px\" class=\"wp-caption aligncenter\"><img aria-describedby=\"caption-attachment-2171281\" loading=\"lazy\" class=\"size-large wp-image-2171281\" src=\"https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?w=680\" alt=\"\" width=\"680\" height=\"510\" srcset=\"https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png 3000w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=150,113 150w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=300,225 300w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=768,576 768w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=680,510 680w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=1536,1152 1536w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=2048,1536 2048w, https://techcrunch.com/wp-content/uploads/2021/06/Karat-Landing-Page_Mobile_Free_Credit_Card_Mockup_20-vup-cobrand.png?resize=50,38 50w\" sizes=\"(max-width: 680px) 100vw, 680px\" /><p id=\"caption-attachment-2171281\" class=\"wp-caption-text\"><strong>Image Credits:</strong> Karat</p></div></p>\n<p>&#8220;Our vetting process is we try to evaluate creators as the businesses they are,&#8221; Wei said. The Karat Black Card doesn&#8217;t charge interest or fees, and only turns a marginal profit off of bank interchange fees. Karat will also advance credit for sponsorship payments at no cost to the creator. So if you&#8217;re an influencer and get paid $1,000 to make a video sponsored by a clothing company, it could take months to get paid. Karat will give you that $1,000 now, so long as you pay them back once the clothing company pays you.</p>\n<p>Karat proved its concept with 50% growth from month to month and eight figures in transactions since launch last year. More than 30 creators have invested in Karat, including <a href=\"https://twitter.com/JaredLeto?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor\">Jared Leto</a>, <a href=\"https://www.instagram.com/3lau/\">3LAU</a>, <a href=\"https://www.facebook.com/nasdaily\">Nas Daily</a>\u00a0and <a href=\"https://www.tiktok.com/@joshrichards?lang=en\">Josh Richards</a> &#8212; that&#8217;s all without any spending on influencer marketing.</p>\n<p>&#8220;It turns out that when you do a good job for creators, they share you around with other people,&#8221; Wei said.</p>\n<p><span style=\"font-size: 1rem; letter-spacing: -0.1px;\"> Since then, their portfolio of investors has grown to include YouTube co-founder Steven Chen, Twitter co-founder Biz Stone, former TikTok CEO Kevin Mayer and former Wealthfront CEO Adam Nash, among others.</span></p>\n<p>But Karat&#8217;s ultimate ambition isn&#8217;t to give creators a line of credit. They started out with the credit card to prove their concept, but in the long term, they hope to create a financial infrastructure for creators. That means helping them launch merchandise lines, incorporate their business, get a mortgage, take out business loans and file their taxes. Wei says that would come after the company&#8217;s Series B, opening a more lucrative income stream than collecting bank interchange fees.</p>\n<p>&#8220;We decided to roll Karat out with the same tried-and-true fintech playbook,&#8221; Wei said. &#8220;Start out with something simple before wedging and scaling into those other products. So for us, the card is just a means to an end. Our whole model is, we use the cards to develop our underwriting model and gain trust from creators, and eventually, we can build to be Square for creators.&#8221;</p>\n<p>Already, Wei and Kim are getting texts from their internet celebrity clients, asking them to be their de-facto financial advisers.</p>\n<p>&#8220;We&#8217;re just like, oh my gosh, we love you, but we&#8217;re not building those products yet,&#8221; Wei said. &#8220;We&#8217;ll do that when we hit our Series B, and yes, we&#8217;ll charge you fees, because we&#8217;re going to provide you with better service than what&#8217;s out there now.&#8221;</p>\n<p>With the newly announced Series A round, Karat plans to double its staff with new hires and begin looking toward new product development.</p>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"4xRlYBrb3a\"><p><a href=\"https://techcrunch.com/2021/06/17/5-tips-for-brands-that-want-to-succeed-in-the-new-era-of-influencer-marketing/\">5 tips for brands that want to succeed in the new era of influencer marketing</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;5 tips for brands that want to succeed in the new era of influencer marketing&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2021/06/17/5-tips-for-brands-that-want-to-succeed-in-the-new-era-of-influencer-marketing/embed/#?secret=4xRlYBrb3a\" data-secret=\"4xRlYBrb3a\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"e6jdzjbpxP\"><p><a href=\"https://techcrunch.com/2020/06/25/karat-black-card/\">Karat launches a credit card for online creators</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;Karat launches a credit card for online creators&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2020/06/25/karat-black-card/embed/#?secret=e6jdzjbpxP\" data-secret=\"e6jdzjbpxP\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n<div class=\"embed breakout\">\n<blockquote class=\"wp-embedded-content\" data-secret=\"Yvta3LLWFv\"><p><a href=\"https://techcrunch.com/2019/11/04/venture-capitalists-like-and-subscribe-to-influencers/\">Venture capitalists \u2018like and subscribe\u2019 to influencers</a></p></blockquote>\n<p><iframe class=\"wp-embedded-content\" sandbox=\"allow-scripts\" security=\"restricted\" style=\"position: absolute; clip: rect(1px, 1px, 1px, 1px);\" title=\"&#8220;Venture capitalists \u2018like and subscribe\u2019 to influencers&#8221; &#8212; TechCrunch\" src=\"https://techcrunch.com/2019/11/04/venture-capitalists-like-and-subscribe-to-influencers/embed/#?secret=Yvta3LLWFv\" data-secret=\"Yvta3LLWFv\" width=\"800\" height=\"450\" frameborder=\"0\" marginwidth=\"0\" marginheight=\"0\" scrolling=\"no\"></iframe></div>\n",
  "date": "Thu, 01 Jul 2021 16:00:16 GMT",
  "id": 2171243,
  "modified": "Thu, 01 Jul 2021 22:22:49 GMT",
  "title": "A bank for the creator economy, Karat Financial raises $26M in Series A funding"
}
```
### Get Authors
This API fetch authors stored in persistent storage<br>
Request Method: GET<br>
Path: /api/v1/authors?offset={int|default 0}&limit={int|default 10}
```
curl --location --request GET 'http://localhost:5000/api/v1/authors?offset=0&limit=3'
{
  "authors": [
    {
      "avatar": "",
      "description": "",
      "id": 133574468,
      "links": {
        "twitter": "https://twitter.com/asilbwrites"
      },
      "name": "Amanda Silberling",
      "position": "",
      "twitter": "asilbwrites"
    },
    {
      "avatar": "false",
      "description": "",
      "id": 133574325,
      "links": [],
      "name": "Walter Thompson",
      "position": "",
      "twitter": ""
    },
    {
      "avatar": "https://techcrunch.com/wp-content/uploads/2021/01/xynitsmpgmmobpekzxkg.jpg.jpg",
      "description": "<p>Brian Heater is the Hardware Editor at TechCrunch. He worked for a number of leading tech publications, including Engadget, PCMag, Laptop, and Tech Times, where he served as the Managing Editor. His writing has appeared in Spin, Wired, Playboy, Entertainment Weekly, The Onion, Boing Boing, Publishers Weekly, The Daily Beast and various other publications. He hosts the weekly Boing Boing interview podcast RiYL, has appeared as a regular NPR contributor and shares his Queens apartment with a rabbit named Lucy.</p>",
      "id": 699688,
      "links": {
        "crunchbase": "https://www.crunchbase.com/person/brian-heater",
        "linkedin": "http://www.linkedin.com/pub/brian-heater/1/a92/94",
        "twitter": "https://twitter.com/bheater"
      },
      "name": "Brian Heater",
      "position": "Hardware Editor",
      "twitter": "bheater"
    },
    {
      "avatar": "https://techcrunch.com/wp-content/uploads/2021/01/r4iwkrm6qsw3n2ximghe.jpg.jpg",
      "description": "<p>Devin Coldewey is a Seattle-based writer and photographer. He first wrote for TechCrunch in 2007. He has also written for MSNBC.com, NBC News, DPReview, The Economist/GE's Look Ahead, and others.</p>\n\n<p>His personal website is coldewey.cc.</p>",
      "id": 12084691,
      "links": {
        "crunchbase": "https://www.crunchbase.com/person/devin-coldewey",
        "homepage": "http://techcrunch.com/author/tcdevin",
        "linkedin": "http://www.linkedin.com/company/techcrunch",
        "twitter": "http://twitter.com/techcrunch"
      },
      "name": "Devin Coldewey",
      "position": "Writer & Photographer",
      "twitter": "techcrunch"
    },
    {
      "avatar": "",
      "description": "",
      "id": 133574433,
      "links": {
        "twitter": "https://twitter.com/breadfrom"
      },
      "name": "Aria Alamalhodaei",
      "position": "",
      "twitter": "breadfrom"
    },
    {
      "avatar": "false",
      "description": "<p>Natasha is a senior reporter for TechCrunch, joining September 2012, based in Europe. She joined TC after a stint reviewing smartphones for CNET UK and, prior to that, more than five years covering business technology for silicon.com (now folded into TechRepublic), where she focused on mobile and wireless, telecoms & networking, and IT skills issues. She has also freelanced for organisations including The Guardian and the BBC. Natasha holds a First Class degree in English from Cambridge University, and an MA in journalism from Goldsmiths College, University of London.</p>",
      "id": 39990176,
      "links": {
        "crunchbase": "https://www.crunchbase.com/person/natasha-lomas",
        "linkedin": "http://www.linkedin.com/in/nlomas",
        "twitter": "https://twitter.com/riptari"
      },
      "name": "Natasha Lomas",
      "position": "Writer",
      "twitter": "riptari"
    },
    {
      "avatar": "https://techcrunch.com/wp-content/uploads/2021/01/diuuw7dfbczpdwmcpldm.png",
      "description": "<p>Ron Miller has been writing about the enterprise at TechCrunch since 2014.</p>\r\n\r\n<p>Previously, he was a long-time Contributing Editor at EContent Magazine. Past regular gigs included CITEworld, DaniWeb, TechTarget, Internet Evolution and FierceContentManagement.</p>\r\n\r\n<p>Disclosures:</p>\r\n\r\n<p>Ron was formerly corporate blogger for Intronis where he wrote once weekly on IT issues. He has contributed to various corporate blogs in the past including Ness, Novell and the IBM Mid-market Blogger Program.</p>",
      "id": 521068,
      "links": {
        "crunchbase": "https://www.crunchbase.com/person/ron-miller",
        "facebook": "",
        "homepage": "https://techcrunch.com/author/ron-miller/",
        "linkedin": "http://www.linkedin.com/in/ronsmiller",
        "twitter": "https://twitter.com/ron_miller"
      },
      "name": "Ron Miller",
      "position": "Enterprise Reporter",
      "twitter": "ron_miller"
    },
    {
      "avatar": "https://techcrunch.com/wp-content/uploads/2021/01/eexgqcxbjbudqhobsoli.jpg.jpg",
      "description": "",
      "id": 70113879,
      "links": {
        "crunchbase": "https://www.crunchbase.com/person/alexandra-ames",
        "facebook": "",
        "homepage": "",
        "linkedin": "",
        "twitter": ""
      },
      "name": "Alexandra Ames",
      "position": "Sr. Marketing Manager",
      "twitter": ""
    },
    {
      "avatar": "false",
      "description": "<p>Lucas Matney is a reporter at TechCrunch and has been covering emerging technologies and startups since 2015. He lives in San Francisco and can be reached via email at lucas@techcrunch.com</p>",
      "id": 89192944,
      "links": {
        "crunchbase": "https://www.crunchbase.com/person/lucas-matney",
        "linkedin": "https://www.linkedin.com/in/lucasmatney/",
        "twitter": "https://twitter.com/lucasmtny"
      },
      "name": "Lucas Matney",
      "position": "Writer",
      "twitter": "lucasmtny"
    },
    {
      "avatar": "",
      "description": "",
      "id": 133574430,
      "links": [],
      "name": "Annie Siebert",
      "position": "",
      "twitter": ""
    }
  ],
  "limit": 10,
  "offset": 0,
  "total_authors": 32
}
```
### Get Author by id
This API fetch author details for given id
Request Method: GET<br>
Path: /api/v1/authors/{author_id}
```
curl --location --request GET 'http://localhost:5000/api/v1/authors/133574468'
{
  "avatar": "",
  "description": "",
  "id": 133574468,
  "links": {
    "twitter": "https://twitter.com/asilbwrites"
  },
  "name": "Amanda Silberling",
  "position": "",
  "twitter": "asilbwrites"
}
```

## TODO
- Unit tests
- Integration Tests

## Possible Future Features
- Fetch others details like tags, categories etc.
- Provide article searching capability via tags and categories.
- Full Text Search 