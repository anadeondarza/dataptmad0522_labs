{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b1af0b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter minimum string length: 2\n",
      "Enter maximum string length: 8\n",
      "How many random strings to generate? 6\n",
      "['5s3sqt1', '4pmvo', 'wpt', 'f6', 'pvmm', '1hloc7']\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "\n",
    "def RandomStringGenerator(l, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):\n",
    "    s = \"\"\n",
    "    return s.join([random.choice(a) for i in range(l)])\n",
    "\n",
    "def BatchStringGenerator(n, a, b):\n",
    "    r = []\n",
    "    for i in range(n):\n",
    "        c = None\n",
    "        if a < b:\n",
    "            c = random.choice(range(a, b))\n",
    "        elif a == b:\n",
    "            c = a\n",
    "        else:\n",
    "            print('Incorrect min and max string lengths. Try again.')\n",
    "            \n",
    "        r.append(RandomStringGenerator(c))\n",
    "    return r\n",
    "\n",
    "a = input('Enter minimum string length: ')\n",
    "b = input('Enter maximum string length: ')\n",
    "n = input('How many random strings to generate? ')\n",
    "\n",
    "print(BatchStringGenerator(int(n), int(a), int(b)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3737f7a0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25039f93",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:jp_env] *",
   "language": "python",
   "name": "conda-env-jp_env-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
