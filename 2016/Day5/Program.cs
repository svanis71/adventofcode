using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode5
{
    class Program
    {
        static string part2(string input)
        {
            var pass = new StringBuilder(8);
            pass.Append("".PadLeft(8));
            using (var md5 = MD5.Create())
            {
                var l = 0;
                while (pass.ToString().Contains(" "))
                {
                    var found = false;
                    while (!found)
                    {
                        var t = Encoding.ASCII.GetBytes($"{input}{l}");
                        var byts = md5.ComputeHash(t);
                        if (byts[0] == 0 && byts[1] == 0 && (byts[2] & 0xF0) == 0)
                        {
                            var pos = byts[2] & 0xf;
                            if (pos < 8 && pass[pos] == ' ')
                            {
                                var ch = (byts[3] >> 4).ToString("X");
                                pass[pos] = ch[0];
                                found = true;
                            }
                        }
                        l++;
                    }
                    Console.WriteLine($"Password: {pass}");
                }
                return pass.ToString();
            }
        }

        static string part1(string input)
        {
            var pass = new StringBuilder();
            using (var md5 = MD5.Create())
            {
                var l = 0;
                for (var i = 0; i < 8; i++)
                {
                    var found = false;
                    while (!found)
                    {
                        var t = Encoding.ASCII.GetBytes($"{input}{l}");
                        var byts = md5.ComputeHash(t);
                        if (byts[0] == 0 && byts[1] == 0 && (byts[2] & 0xF0) == 0)
                        {
                            pass.Append(byts[2].ToString("X"));
                            found = true;
                        }
                        l++;
                    }
                    Console.WriteLine($"Password: {pass}");
                }

                return pass.ToString();
            }
        }

        static void Main(string[] args)
        {
            var input = "uqwqemis";
            part1(input);
            part2(input);
            Console.ReadKey();
        }
    }
}
