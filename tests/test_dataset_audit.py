import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from breast_histopathology.dataset_audit import (
    count_patches,
    parse_patch_filename,
    patient_overlap,
)


class DatasetAuditTests(unittest.TestCase):
    def test_extract_patient_and_binary_label(self):
        self.assertEqual(
            parse_patch_filename('9345_idx5_x2001_y151_class1.png'), ('9345', 1)
        )
        self.assertEqual(
            parse_patch_filename('12890_idx5_x801_y1451_class0.png'), ('12890', 0)
        )
        self.assertIsNone(parse_patch_filename('unexpected-name.png'))

    def test_counts_and_skipped_files(self):
        summary = count_patches([
            '9345_idx5_x1_y1_class1.png',
            '9345_idx5_x2_y3_class0.png',
            '12890_idx5_x3_y4_class0.png',
            'other.png',
        ])
        self.assertEqual(summary, dict(
            matched_patches=3, positive_patches=1, negative_patches=2,
            unique_patients=2, unmatched_files=1
        ))

    def test_patient_overlap_detects_leakage(self):
        overlap = patient_overlap({
            'train': ['9345_idx5_x1_y1_class0.png'],
            'validation': ['12890_idx5_x1_y2_class0.png'],
            'test': ['9345_idx5_x2_y2_class1.png'],
        })
        self.assertEqual(overlap, {'9345': ['test', 'train']})

    def test_no_cross_patient_overlap(self):
        overlap = patient_overlap({
            'train': ['9345_idx5_x1_y1_class0.png'],
            'test': ['12890_idx5_x1_y1_class1.png'],
        })
        self.assertEqual(overlap, {})


if __name__ == '__main__':
    unittest.main()
