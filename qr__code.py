{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/w8ZGEKX+kB+76tHcQSWf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/umang25bce10803-ctrl/qr-code-generator/blob/main/qr__code.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VbEn5uYI_XUw",
        "outputId": "d8d252dc-c6cc-42c8-ed0c-47692a9e3a4d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "enter the data you want to generate qr for:google.com\n"
          ]
        }
      ],
      "source": [
        "#qr code library\n",
        "import qrcode\n",
        "\n",
        "data = input(\"enter the data you want to generate qr for:\")\n",
        "\n",
        "qr = qrcode.QRCode(version = 1,\n",
        "                   box_size = 10,\n",
        "                   border = 5)\n",
        "\n",
        "qr.add_data(data)\n",
        "\n",
        "qr.make(fit = True)\n",
        "img = qr.make_image(fill_color = 'red',\n",
        "                    back_color = 'white')\n",
        "\n",
        "img.save('MyQRCode2.png')"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "AcJT25jC_f4Y"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
