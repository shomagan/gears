import os
import sys
import time
import _thread as thread
import msvcrt

try:
    __import__('rich')
except ImportError:
    print("Installing rich ")
    from setuptools.command.easy_install import main as install
    install(['rich'])

from rich.console import Console
from rich.table import Column, Table
from rich.columns import Columns
from rich.live import Live

pictures0 = ["                      \n"\
            "                      \n"\
            "                      \n"\
            "          *           \n"\
            "           **         \n"\
            "          *..*        \n"\
            "          * -*        \n"\
            "    *      **     *   \n"\
            "     *** ****** **    \n"\
            "        * * *  *      \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "         ***  ***     \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "           **         \n"\
            "          *..*        \n"\
            "        * * -*        \n"\
            "           **         \n"\
            "    **** ****** ***   \n"\
            "        * * *  *      \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "          **   **     \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "           **         \n"\
            "          *..*        \n"\
            "          * -*        \n"\
            "         * **         \n"\
            "     *** ****** **    \n"\
            "    *   * * *  * *    \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "           **         \n"\
            "          *..*        \n"\
            "          *- *        \n"\
            "           ** *       \n"\
            "      ** ****** *     \n"\
            "    *   * * *  * *    \n"\
            "   *   *        * *   \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "       *     *        \n"\
            "                      \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "           **         \n"\
            "          *..* *      \n"\
            "          *- *        \n"\
            "           **         \n"\
            "      ** ****** *     \n"\
            "   **   * * *  * **   \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "        **    *       \n"\
            "             *        \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "           ** **      \n"\
            "          *..*        \n"\
            "          *- *        \n"\
            "           **         \n"\
            "    **** ****** ****  \n"\
            "        * * *  *      \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "        **   **       \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "               *      \n"\
            "              **      \n"\
            "           **         \n"\
            "          *..*        \n"\
            "          *- *      * \n"\
            "     *     **     *   \n"\
            "      ** ****** *     \n"\
            "        * * *  *      \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "        **   **       \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "           *          \n"\
            "           *          \n"\
            "           **         \n"\
            "          *..*        \n"\
            "          * 0    *    \n"\
            "           **   *     \n"\
            "    * ** ****** *     \n"\
            "        *  *  **      \n"\
            "       *        *     \n"\
            "      ************    \n"\
            "         *    *       \n"\
            "         **   **      \n"\
            "                      \n",            ]
pictures1= ["                      \n"\
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          * -*        \n"\
            "    *     ****    *   \n"\
            "     *** ****** **    \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "         ***  ***     \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          * -*        \n"\
            "          ****        \n"\
            "    **** ****** ***   \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "          **   **     \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          * -*        \n"\
            "          ****        \n"\
            "     *** ****** **    \n"\
            "    *    *    *  *    \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          *- *        \n"\
            "          ****        \n"\
            "      ** ****** *     \n"\
            "    *    *    *  *    \n"\
            "   *     *    *   *   \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "       *     *        \n"\
            "                      \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          *- *        \n"\
            "          ****        \n"\
            "      ** ****** *     \n"\
            "   **    *    *  **   \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "        **    *       \n"\
            "             *        \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          *- *        \n"\
            "          ****        \n"\
            "    **** ****** ****  \n"\
            "         *    *       \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "        **   **       \n"\
            "                      \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          *- *      * \n"\
            "     *    ****    *   \n"\
            "      ** ****** *     \n"\
            "         ** * *       \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "        **   **       \n"\
            "                      \n",
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "                      \n"\
            "          ****        \n"\
            "          *..*        \n"\
            "          * 0*   *    \n"\
            "          ****  *     \n"\
            "    * ** ****** *     \n"\
            "         * *  *       \n"\
            "         *    *       \n"\
            "         ******       \n"\
            "         *    *       \n"\
            "         **   **      \n"\
            "                      \n",            ]

class TableStates():
    rows = 1
    columns = 1
    counter = 0

def dance(height: int, table_state: int):
    items = len(pictures0)
    table = Table("", "")
    table.add_row(pictures0[table_state.counter%items],
            pictures1[table_state.counter%items],)

    return (table)



def main():
    engagement = input("What year was the engagement?")  # tutu
    if engagement != "2012":
        print("try again")
        return
    month = input("month of the first kiss?")  # tutu
    if month != "may":
        print("try again")
        return
    discipline = input("our favorite discipline at the institute?")  # tutu
    if discipline != "economy":
        print("try again")
        return

    console = Console()
    with Live(console=console, transient=True, auto_refresh=False) as live:
        table_state = TableStates()
        while True:
            live.update(dance(console.size.height - 4, table_state), refresh=True)
            table_state.counter += 1
            time.sleep(0.1)


if __name__ == "__main__":
    main()