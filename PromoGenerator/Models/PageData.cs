using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Collections.ObjectModel;

public class PageData
{
    public string Line1 { get; set; }
    public string Line2 { get; set; }
    public string Speaker { get; set; }
    public string Receiver { get; set; }
    public string Taunt { get; set; }
    public string Demeanor { get; set; }

    public ObservableCollection<FeatureData> Features { get; set; }
        = new ObservableCollection<FeatureData>();
}