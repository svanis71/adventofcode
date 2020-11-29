using System;
using System.Collections.Generic;
using System.Net.NetworkInformation;
using System.Security.Cryptography;
using System.Text;

namespace Day14
{

    static class Extras
    {
        public static string MakeString(this byte[] bytes)
        {
            var sb = new StringBuilder();
            foreach (var b in bytes)
            {
                sb.Append(b.ToString("x2"));
            }
            return sb.ToString();
        }
    }

    static class Program
    {
        static byte[] Stretch(byte[] orig, MD5 md5)
        {
            var str = orig.MakeString();
            byte[] hash1 = null;
            for (var i = 0; i < 2016; i++)
            {
                hash1 = md5.ComputeHash(Encoding.ASCII.GetBytes(str));
                str = hash1.MakeString();
            }
            return hash1;
        }

        static int part2(string input)
        {
            var l = 0;
            using (var md5 = MD5.Create())
            {
                for (var i = 0; i < 64; i++)
                {
                    var found = false;
                    while (!found)
                    {
                        var code1 = Encoding.ASCII.GetBytes($"{input}{l}");
                        var hash1 = Stretch(md5.ComputeHash(code1), md5);

                        char tripleChar = checkTriple(hash1);
                        if (tripleChar != ' ')
                        {
                            for (var k = l + 1; !found && k < l + 1001; k++)
                            {
                                var data = $"{input}{k}";
                                var ib = Encoding.ASCII.GetBytes(data);
                                var hash5 = Stretch(md5.ComputeHash(ib), md5);
                                found = hasFiveEqual(hash5, tripleChar);
                                if (found)
                                {
                                    Console.WriteLine($"at {l} ({i})");
                                }
                            }
                        }
                        l++;
                    }
                }

                return l;
            }
        }

        static int part1(string input)
        {
            var l = 0;
            using (var md5 = MD5.Create())
            {
                for (var i = 0; i < 64; i++)
                {
                    var found = false;
                    while (!found)
                    {
                        var code1 = Encoding.ASCII.GetBytes($"{input}{l}");
                        var hash1 = md5.ComputeHash(code1);
                        char tripleChar = checkTriple(hash1);
                        if (tripleChar != ' ')
                        {
                            for (var k = l + 1; !found && k < l + 1001; k++)
                            {
                                var data = $"{input}{k}";
                                var ib = Encoding.ASCII.GetBytes(data);
                                var hash5 = md5.ComputeHash(ib);
                                found = hasFiveEqual(hash5, tripleChar);
                                if (found)
                                {
                                    Console.WriteLine($"at {l} ({i})");
                                }
                            }

                        }
                        l++;
                    }
                }

                return l;
            }
        }

        private static char checkTriple(byte[] hash1)
        {
            bool hasTriple = false;
            char tripleChar = ' ';
            for (var p = 0; !hasTriple && p < hash1.Length; p++)
            {
                var hex = hash1[p].ToString("x2");
                if (hex[0] == hex[1])
                {
                    var prev = p > 0 ? hash1[p - 1].ToString("x2") : "  ";
                    var next = p < hash1.Length - 1 ? hash1[p + 1].ToString("x2") : "  ";
                    if (prev[1] == hex[0] || next[0] == hex[0])
                    {
                        // Found triple
                        hasTriple = true;
                        tripleChar = hex[0];
                    }
                }
            }
            return tripleChar;
        }

        private static bool hasFiveEqual(byte[] hash5, char testCh)
        {
            bool found = false;
            for (var m = 0; !found && m < hash5.Length - 1; m++)
            {
                var hex1 = hash5[m].ToString("x2");
                var hex2 = hash5[m + 1].ToString("x2");
                if (hex1[0] == testCh && hex1[0] == hex1[1] && hex2 == hex1)
                {
                    var prevF = m > 0 ? hash5[m - 1].ToString("x2") : "  ";
                    var nextF = m < hash5.Length - 2 ? hash5[m + 2].ToString("x2") : "  ";
                    if (prevF[1] == hex1[0] || nextF[0] == hex2[1])
                    {
                        found = true;
                        Console.Write($"Found key same char {testCh}! {prevF[1]}{hex1}{hex2}{nextF[0]} ");
                    }
                }
            }
            return found;
        }

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            var input = "ahsbgdzn";
            //part1(input);
            part2(input);
            Console.ReadKey();
        }
    }
}
