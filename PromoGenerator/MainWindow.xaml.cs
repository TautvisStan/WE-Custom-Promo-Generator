using Microsoft.Win32;
using System;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Windows;
using System.Windows.Controls;

namespace PromoGenerator
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public ObservableCollection<string> IdList { get; set; }
            = new ObservableCollection<string>();

        public ObservableCollection<PageData> Pages { get; set; }
            = new ObservableCollection<PageData>();

        public MainWindow()
        {
            InitializeComponent();
            DataContext = this;

            IdList.Add("No wrestlers");
        }
        private void UpdateSpeakers_Click(object sender, RoutedEventArgs e)
        {
            IdList.Clear();

            if (!int.TryParse(WrestlersTextBox.Text, out int wrestlers))
            {
                IdList.Add("Invalid wrestler count");
                return;
            }

            bool team1 = Team1CheckBox.IsChecked == true;
            bool team2 = Team2CheckBox.IsChecked == true;
            bool hasRef = RefCheckBox.IsChecked == true;

            if (wrestlers == 0 && !team1 && !team2 && !hasRef)
            {
                IdList.Add("No wrestlers");
                return;
            }

            for (int i = 0; i < wrestlers; i++)
            {
                IdList.Add($"Wrestler {i + 1} speaker id: {i + 1}");
            }

            int currentId = wrestlers;

            if (team1)
            {
                currentId++;
                IdList.Add($"Wrestler 1 team member speaker id: {currentId}");
            }

            if (team2)
            {
                currentId++;
                IdList.Add($"Wrestler 2 team member speaker id: {currentId}");
            }

            if (hasRef)
            {
                currentId++;
                IdList.Add($"Ref speaker id: {currentId}");
            }
        }

        private void AddPage_Click(object sender, RoutedEventArgs e)
        {
            Pages.Add(new PageData());
        }
        private void DeletePage_Click(object sender, RoutedEventArgs e)
        {
            if (sender is FrameworkElement fe && fe.DataContext is PageData page)
            {
                Pages.Remove(page);
            }
        }
        private void AddFeature_Click(object sender, RoutedEventArgs e)
        {
            if (sender is FrameworkElement fe && fe.DataContext is PageData page)
            {
                page.Features.Add(new FeatureData());
            }
        }
        private void DeleteFeature_Click(object sender, RoutedEventArgs e)
        {
            if (sender is Button btn && btn.Tag is FeatureData feature)
            {
                foreach (var page in Pages)
                {
                    if (page.Features.Contains(feature))
                    {
                        page.Features.Remove(feature);
                        break;
                    }
                }
            }
        }

        private void SavePromo_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                string promoText = GeneratePromoText();

                var dialog = new SaveFileDialog
                {
                    Filter = "Promo files (*.promo)|*.promo|All files (*.*)|*.*",
                    FileName = TitleTextBox.Text + ".promo",
                    InitialDirectory = Directory.GetCurrentDirectory()
                };

                if (dialog.ShowDialog() == true)
                {
                    File.WriteAllText(dialog.FileName, promoText);
                    MessageBox.Show(".promo file was successfully generated!", "Success");
                }
            }
            catch (HandledException ex)
            {
                MessageBox.Show(ex.Message.ToString(), "Error!");
            }
            catch (Exception ex)
            {
                File.WriteAllText("log.txt", ex.ToString());
                MessageBox.Show("An error has occurred. Check log.txt", "Error!");
            }
        }
        private void ClearAll()
        {
            TitleTextBox.Clear();
            DescriptionTextBox.Clear();
            WrestlersTextBox.Clear();

            Team1CheckBox.IsChecked = false;
            Team2CheckBox.IsChecked = false;
            RefCheckBox.IsChecked = false;

            IdList.Clear();
            IdList.Add("No wrestlers");

            Pages.Clear();
        }
        private void New_Click(object sender, RoutedEventArgs e)
        {
            ClearAll();
        }
        private void Open_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new OpenFileDialog
            {
                Filter = "Promo files (*.promo)|*.promo|All files (*.*)|*.*"
            };

            if (dialog.ShowDialog() == true)
            {
                try
                {
                    LoadPromo(dialog.FileName);
                }
                catch (HandledException ex)
                {
                    MessageBox.Show(ex.Message.ToString(), "Error!");
                }
                catch (Exception ex)
                {
                    File.WriteAllText("log.txt", ex.ToString());
                    MessageBox.Show("Failed to load the file.", "Error!");
                }
            }
        }
        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
        private void About_Click(object sender, RoutedEventArgs e)
        {
            Process.Start(new ProcessStartInfo
            {
                FileName = "https://steamcommunity.com/sharedfiles/filedetails/?id=3038504814",
                UseShellExecute = true
            });
        }

        private string GeneratePromoText()
        {
            var sb = new StringBuilder();

            string title = TitleTextBox.Text;
            if (string.IsNullOrWhiteSpace(title))
                throw new HandledException("No title");

            string description = DescriptionTextBox.Text;
            if (string.IsNullOrWhiteSpace(description))
                throw new HandledException("No description");

            if (!int.TryParse(WrestlersTextBox.Text, out int wrestlers))
                throw new HandledException("Invalid wrestlers");

            bool team1 = Team1CheckBox.IsChecked == true;
            bool team2 = Team2CheckBox.IsChecked == true;
            bool hasRef = RefCheckBox.IsChecked == true;
            bool useNames = UseNamesCheckBox?.IsChecked == true;

            string surprises = SurpriseEntrantsTextBox?.Text ?? "";
            string nextPromo = NextPromoTextBox?.Text ?? "";
            string probability = ProbabilityTextBox?.Text ?? "";

            if (Pages.Count == 0)
                throw new HandledException("No pages");

            // Header
            sb.AppendLine($"title: {title}");
            sb.AppendLine($"description: {description}");

            // Characters
            sb.Append("characters: ");
            for (int i = 0; i < wrestlers; i++)
            {
                if (i > 0) sb.Append(",");
                sb.Append(i + 1);
            }

            if (team1) sb.Append(",11");
            if (team2) sb.Append(",22");
            if (hasRef) sb.Append(",-1");

            sb.AppendLine();

            if (useNames)
                sb.AppendLine("use_names: True");

            if (!string.IsNullOrWhiteSpace(surprises))
                sb.AppendLine($"surprise_entrants: {surprises}");

            if (!string.IsNullOrWhiteSpace(nextPromo))
                sb.AppendLine($"next_promo: {nextPromo}");

            if (!string.IsNullOrWhiteSpace(probability))
                sb.AppendLine($"career_probability: {probability}");

            // Pages
            foreach (var page in Pages)
            {
                string line1 = page.Line1 ?? "";
                string line2 = page.Line2 ?? "";

                int speaker = int.TryParse(page.Speaker, out var s) ? s : 0;
                int receiver = int.TryParse(page.Receiver, out var r) ? r : 0;
                int taunt = int.TryParse(page.Taunt, out var t) ? t : 0;

                int demeanor = 0;
                if (page.Demeanor == "H") demeanor = 50;
                else if (page.Demeanor == "A") demeanor = -50;

                sb.Append($"\"{line1}\",\"{line2}\",{speaker},{receiver},{taunt},{demeanor}");

                if (page.Features.Count > 0)
                {
                    sb.Append(",");
                    var featureText = string.Join(";", page.Features.Select(f => f.FeatureText));
                    sb.Append(featureText);
                }

                sb.AppendLine();
            }

            return sb.ToString();
        }
        private void LoadPromo(string filename)
        {
            ClearAll();

            var lines = File.ReadAllLines(filename);
            int index = 0;

            // Title
            TitleTextBox.Text = lines[index].Substring(7).Trim();
            index++;

            // Description
            DescriptionTextBox.Text = lines[index].Substring(13).Trim();
            index++;

            // Characters
            var wrestlerParts = lines[index].Substring(12).Trim().Split(',');
            index++;

            int wrestlers = 0;
            bool team1 = false;
            bool team2 = false;
            bool hasRef = false;

            foreach (var part in wrestlerParts)
            {
                if (part == "1" || part == "2" || part == "3")
                    wrestlers++;
                else if (part == "11")
                    team1 = true;
                else if (part == "22")
                    team2 = true;
                else if (part == "-1")
                    hasRef = true;
            }

            WrestlersTextBox.Text = wrestlers.ToString();
            Team1CheckBox.IsChecked = team1;
            Team2CheckBox.IsChecked = team2;
            RefCheckBox.IsChecked = hasRef;

            UpdateSpeakers_Click(null, null); // refresh ID display

            // Optional fields
            while (index < lines.Length)
            {
                var line = lines[index];

                if (line.StartsWith("use_names:"))
                {
                    UseNamesCheckBox.IsChecked =
                        line.Substring(11).Trim().ToLower() == "true";
                }
                else if (line.StartsWith("surprise_entrants:"))
                {
                    SurpriseEntrantsTextBox.Text =
                        line.Substring(19).Trim();
                }
                else if (line.StartsWith("next_promo:"))
                {
                    NextPromoTextBox.Text =
                        line.Substring(12).Trim();
                }
                else if (line.StartsWith("career_probability:"))
                {
                    ProbabilityTextBox.Text =
                        line.Substring(20).Trim();
                }
                else
                {
                    break;
                }

                index++;
            }

            // Pages
            for (; index < lines.Length; index++)
            {
                var line = lines[index];

                var parts = Regex.Split(line, ",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");

                var page = new PageData();

                page.Line1 = parts[0].Trim('"');
                page.Line2 = parts[1].Trim('"');
                page.Speaker = parts[2];
                page.Receiver = parts[3];

                page.Taunt = parts.Length > 4 ? parts[4] : "0";

                if (parts.Length > 5 && int.TryParse(parts[5], out int d))
                {
                    if (d > 0) page.Demeanor = "H";
                    else if (d < 0) page.Demeanor = "A";
                    else page.Demeanor = "0";
                }

                // Features
                if (parts.Length > 6)
                {
                    var features = parts[6].Split(';');

                    foreach (var f in features)
                    {
                        page.Features.Add(new FeatureData
                        {
                            FeatureText = f.Trim()
                        });
                    }
                }

                Pages.Add(page);
            }
        }
    }
}
