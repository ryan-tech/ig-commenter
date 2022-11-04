import requests
import random
import time

def getRandomComment():
    commentBank = [
        'hi aphig', 
        'Start each day with a positive thought and a grateful heart. - Roy T. Bennett',
        'Today is your day. Your mountain is waiting so get on your way.- Dr. Seuss',
        'Light tomorrow with today. -Elizabeth Barrett Browning',
        'Yesterday is not ours to recover, but tomorrow is ours to win or lose. - Lyndon B. Johnson',
        'When it rains, it pours? but soon, the sun shines again. Stay positive. Better days are on their way.',
        'Learn the rules like a pro, so you can break them like an artist. -Pablo Picasso',
        'Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway. - Earl Nightingale',
        'Just one small positive thought in the morning can change your whole day. - Dalai Lama',
        'Push yourself because no one else is going to do it for you.',
        'Yesterday is not ours to recover, but tomorrow is ours to win or lose. -Lyndon Johnson',
        'Every object, every being, is a jar of delight. Be a connoisseur.- Rumi',
        'Yesterdays home runs dont win todays games. - Babe Ruth',
        'Someday is not a say of the week. - Janet Dailey',
        'Youre off to great places, today is your day. Your mountain is waiting, so get on your way. - Dr. Seuss',
        'Dont count the days, make the days count. - Muhammad Ali',
        'Make each day your masterpiece. - John Wooden',
        'Youre braver than you believe and stronger than you seem, and smarter than you think. - A.A Mine',
        'Wonder is the beginning of wisdom. - Socrates',
        'How wonderful it is that nobody need wait a single moment before starting to improve the world. -Anne Frank',
        'Believe you can and youre halfway there. - Theodore Roosevelt',
        'Dont judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson',
        'Every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact. - Les Brown',
        'Youve got to get up every morning with determination if youre going to go to bed with satisfaction. - George Lorimer',
        'When you want something, all the universe conspires in helping you to achieve it. - Paulo Coelho'
    ]
    random_index = random.randint(0,len(commentBank)-1)
    return commentBank[random_index]

def run():
    cookies = {
        # get from curlconverter [ read README ]
    }
    headers = {
        # get from curlconverter [ read README ]
    }
    statusCodeHolder = 200
    commentsWritten = 0
    while(statusCodeHolder == 200):
        data = {
            'comment_text': getRandomComment(),
        }
        response = requests.post('https://www.instagram.com/api/v1/web/comments/2961354355224985324/add/', cookies=cookies, headers=headers, data=data)
        print(data)
        print(response.content)
        statusCodeHolder = response.status_code
        print(response.status_code)
        commentsWritten += 1
        print('comments written: {}'.format(commentsWritten))
        time.sleep(60)
        



if __name__ == "__main__":
    run()
    
    